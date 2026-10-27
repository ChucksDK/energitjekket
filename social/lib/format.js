const intl = (decimals) =>
  new Intl.NumberFormat('da-DK', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
    useGrouping: 'always',
  });

// Værdier der runder til nul (fx -0,001) skal vises som "0,00", ikke "-0,00".
const nf = (decimals) => {
  const f = intl(decimals);
  return {
    format: (v) => {
      const s = f.format(v);
      return /^[-\u2212][0.,]+$/.test(s) ? s.slice(1) : s;
    },
  };
};

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
