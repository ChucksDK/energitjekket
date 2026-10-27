const nf = (decimals) =>
  new Intl.NumberFormat('da-DK', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
    useGrouping: 'always',
  });

const RULES = {
  kr: (v) => `${nf(0).format(v)} kr.`,
  kr_per_kwh: (v) => `${nf(2).format(v)} kr.`,
  kwh: (v) => `${nf(0).format(v)} kWh`,
  kwh_per_kwp: (v) => `${nf(0).format(v)} kWh`,
  pct: (v) => `${nf(0).format(v)} %`,
  hour: (v) => `kl. ${String(v).padStart(2, '0')}`,
  m2: (v) => `${nf(0).format(v)} m²`,
  kwp: (v) => `${nf(0).format(v)} kWp`,
  count: (v) => nf(0).format(v),
  scop: (v) => nf(1).format(v),
};

export function formatFact(value, unit) {
  const rule = Object.hasOwn(RULES, unit) ? RULES[unit] : undefined;
  if (!rule) throw new Error(`formatFact: unknown unit "${unit}"`);
  return rule(value);
}
