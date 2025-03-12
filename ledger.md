---
name: "report_{from}_{to}.md"
params:
  from:
    required: true
  to:
    required: true
  file:
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

## Ending balance:

{{hledger -f $file bal -e $to -t}}

## Transactions:

{{hledger -f $file print -b $from -e $to}}
