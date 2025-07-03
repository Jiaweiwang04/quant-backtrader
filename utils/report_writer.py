import os

def save_analysis_report(strategy, filename="sma_crossover_report.md", initial_cash=10000, final_value=None):
    """
    Save analysis result as Markdown 
    """

    sharpe_result = strategy.analyzers.sharpe.get_analysis()
    drawdown_result = strategy.analyzers.drawdown.get_analysis()

    report = f"""# Backtest Summary Report

**Initial Portfolio Value**: {initial_cash}  
**Final Portfolio Value**: {final_value:.2f}

## Sharpe Ratio
{sharpe_result}

## Max Drawdown
{drawdown_result}
"""

    path = os.path.join("docs", filename)
    with open(path, "w") as f:
        f.write(report)

    print(f"save report to {path}")
