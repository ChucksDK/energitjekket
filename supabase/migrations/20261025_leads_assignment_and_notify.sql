-- Tildeling til ét firma + notifikationer (notify-recipient edge function)
alter table public.leads
  add column assigned_company_name text check (assigned_company_name is null or char_length(btrim(assigned_company_name)) between 2 and 200),
  add column assigned_company_cvr  text check (assigned_company_cvr is null or assigned_company_cvr ~ '^[0-9]{8}$'),
  add column assigned_at           timestamptz,
  add column customer_notified_at  timestamptz,
  add column owner_notified_at     timestamptz,
  add column notify_error          text check (notify_error is null or char_length(notify_error) <= 2000);

-- anon må kun indsætte formularfelterne (ikke tildelings-/notifikationskolonner)
revoke insert on table public.leads from anon;
grant insert (service, city, page_url, answers, name, email, phone, postal_code,
              consent_text, consent_version, user_agent, utm) on table public.leads to anon;

-- sæt assigned_at automatisk, når firmaet udfyldes
create or replace function public.leads_set_assigned_at()
returns trigger language plpgsql set search_path = '' as $$
begin
  if new.assigned_company_name is not null and new.assigned_company_cvr is not null
     and (old.assigned_company_name is distinct from new.assigned_company_name
          or old.assigned_company_cvr is distinct from new.assigned_company_cvr) then
    new.assigned_at := now();
  end if;
  return new;
end $$;
create trigger leads_assigned_at before update on public.leads
  for each row execute function public.leads_set_assigned_at();

create extension if not exists pg_net with schema extensions;

-- kald edge function asynkront (fejler aldrig selve INSERT/UPDATE)
create or replace function public.leads_notify()
returns trigger language plpgsql security definer set search_path = '' as $$
declare kind text;
begin
  if tg_op = 'INSERT' then
    kind := 'INSERT';
  elsif new.assigned_company_name is not null and new.assigned_company_cvr is not null
        and (old.assigned_company_name is distinct from new.assigned_company_name
             or old.assigned_company_cvr is distinct from new.assigned_company_cvr) then
    kind := 'ASSIGNED';
  else
    return new;
  end if;
  begin
    perform net.http_post(
      url := 'https://ckdrjxjdxprezsvfdpet.supabase.co/functions/v1/notify-recipient',
      body := jsonb_build_object('type', kind, 'lead_id', new.id),
      headers := '{"Content-Type":"application/json"}'::jsonb,
      timeout_milliseconds := 10000);
  exception when others then
    raise warning 'leads_notify: %', sqlerrm;
  end;
  return new;
end $$;
revoke all on function public.leads_notify() from public, anon, authenticated;
revoke all on function public.leads_set_assigned_at() from public, anon, authenticated;

create trigger leads_notify_insert after insert on public.leads
  for each row execute function public.leads_notify();
create trigger leads_notify_assigned after update of assigned_company_name, assigned_company_cvr on public.leads
  for each row execute function public.leads_notify();
