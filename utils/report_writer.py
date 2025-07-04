import os

def save_analysis_report(strategy, filename="sma_crossover_report.md", initial_cash=10000, final_value=None):

    sharpe_dict = strategy.analyzers.sharpe.get_analysis()
    sharpe_ratio = sharpe_dict.get('sharperatio', 'N/A')
    sharpe_ratio_str = f"{sharpe_ratio:.4f}" if isinstance(sharpe_ratio, (float, int)) else str(sharpe_ratio)

    drawdown_dict = strategy.analyzers.drawdown.get_analysis()
    max_dd = drawdown_dict.get('max', {})
    max_dd_val = max_dd.get('drawdown', 'N/A')
    moneydown = max_dd.get('moneydown', 'N/A')
    dd_len = max_dd.get('len', drawdown_dict.get('len', 'N/A'))

    max_dd_str = f"{max_dd_val:.2f}%" if isinstance(max_dd_val, (float, int)) else str(max_dd_val)
    moneydown_str = f"{moneydown:.2f}" if isinstance(moneydown, (float, int)) else str(moneydown)

    report = f"""# Backtest Summary Report

**Initial Portfolio Value**: {initial_cash}  
**Final Portfolio Value**: {final_value:.2f}

## Sharpe Ratio
Sharpe Ratio: {sharpe_ratio_str}

## Max Drawdown
Max Drawdown: {max_dd_str}  
Money Lost: ¥{moneydown_str}  
Duration (days): {dd_len}
"""

    path = os.path.join("docs", filename)
    with open(path, "w") as f:
        f.write(report)

    print(f"Analysis report saved to {path}")
