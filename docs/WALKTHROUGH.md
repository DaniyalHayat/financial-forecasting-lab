# Workbook walkthrough

## Business question
Which operating drivers explain the profit shortfall, and how much cash remains if demand weakens while inventory turns slow?

1. Open Summary for the EBITDA variance and ending cash in the synthetic case.
2. On Variance bridge, check that the drivers reconcile to actual EBITDA less budget. The volume effect uses the budget-weighted margin. The mix effect captures changes in what sold.
3. Set Assumptions D5 to 2 for the downside case. Lower demand, weaker pricing, higher costs, slower inventory turns, and shorter supplier terms all reduce ending cash.
4. Trace merchandise COGS into inventory and accounts payable. Fulfillment is expensed. The cash flow adds back depreciation as a noncash expense.
5. Filter the PivotTable by region, then read the [management memo](../outputs/management_memo.md) for proposed actions and assumptions to verify.

## Forecast assumptions

- The synthetic generator includes holiday seasonality, which favors the seasonal forecast in the holdout.
- Backtest predictions use only 2025 inputs. The forward forecast uses data through June 2026.
- With 18 months of data, the forecast uses a seasonal baseline and an explicit financial-driver model.
- A live implementation would need verified source mappings, merchandise-ledger balances, and calibrated demand responses before its forecasts could guide decisions.
