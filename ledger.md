---
name: "report_{from}_{to}.md"
params:
  from:
    type: str
    required: true
  to:
    type: str
    required: true
  file:
    type: str
    default: ledger.j
---

# Finance Report from {from} to {to}

## Previous status:

{{hledger -f $file bal -e $from -t}}

```

              $66606  assets:bank
               $4775  expenses:server
             $-71381  income
             $-71080    award
                 $-1    interest
               $-300    salary
--------------------
                   0
```

## Expenses:

{{hledger -f $file reg expenses -b $from -e $end}}

```

2024-08-31 Porkbun Domain Re..  expenses:domain               $345          $345
2024-08-31 Google Cloud Aug     expenses:server               $980         $1325
2024-09-30 Google Cloud Sep     expenses:server               $811         $2136
2024-10-31 Google Cloud Oct     expenses:server               $677         $2813
2024-11-30 Google Cloud Nov     expenses:server               $767         $3580
2024-12-31 Google Cloud Dec     expenses:server               $902         $4482
2025-01-31 Google Cloud Jan     expenses:server               $911         $5393
2025-02-28 Google Cloud Feb     expenses:server               $760         $6153
2025-03-11 Spaceship Domain ..  expenses:domain               $255         $6408
```

## Ending balance:

{{hledger -f $file bal -e $to -t}}

```

              $67403  assets:bank
              $11183  expenses
                $600    domain
              $10583    server
             $-78586  income
             $-78283    award
                 $-3    interest
               $-300    salary
--------------------
                   0
```

## Transactions:

{{hledger -f $file print -b $from -e $to}}

```

2024-08-31 Porkbun Domain Renewal
    expenses:domain               $345
    liabilities:justin

2024-08-31 Google Cloud Aug
    expenses:server               $980
    liabilities:justin

2024-09-30 Google Cloud Sep
    expenses:server               $811
    liabilities:justin

2024-10-07 預提支出
    liabilities:justin           $2005
    assets:bank

2024-10-31 Google Cloud Oct
    expenses:server               $677
    liabilities:justin

2024-11-26 g0v 獎金
    assets:bank            $7203
    income:award

2024-11-30 Google Cloud Nov
    expenses:server               $767
    liabilities:justin

2024-12-21 利息
    assets:bank                  $2
    income:interest

2024-12-31 Google Cloud Dec
    expenses:server               $902
    liabilities:justin

2025-01-31 Google Cloud Jan
    expenses:server               $911
    liabilities:justin

2025-02-28 Google Cloud Feb
    expenses:server               $760
    liabilities:justin

2025-03-11 Spaceship Domain root4.dev
    expenses:domain               $255
    liabilities:justin

2025-03-11 付清代壂支出
    liabilities:justin           $4403
    assets:bank

```
