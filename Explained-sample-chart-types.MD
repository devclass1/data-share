```python
# Import required libraries
import plotly.graph_objects as go  # Main Plotly graphing library
from plotly.subplots import make_subplots  # For creating multi-plot layouts
import pandas as pd  # For data manipulation
import numpy as np  # For numerical operations
from datetime import datetime  # For date handling

# Set random seed for reproducible results
np.random.seed(42)

# ======================
# 1. SAMPLE DATA PREP
# ======================

# Create list of months for x-axis
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Generate random sales data (80,000 to 200,000 in steps of 1,000)
sales = np.random.randint(80, 200, 6) * 1000

# Calculate expenses as 30-50% of sales
expenses = sales * np.random.uniform(0.3, 0.5, 6)

# Create date range for daily data (January 2023)
date_range = pd.date_range("2023-01-01", "2023-01-31")

# Generate cumulative daily sales with normal distribution
daily_sales = np.random.normal(5000, 1500, 31).cumsum()

# Product names and random sales figures
products = ['Widget A', 'Widget B', 'Widget C']
product_sales = np.random.randint(20, 60, 3) * 1000

# ======================
# 2. CREATE DASHBOARD LAYOUT
# ======================

# Create 2x2 grid layout with different chart types
fig = make_subplots(
    rows=2, cols=2,  # 2 rows, 2 columns
    specs=[  # Chart type specifications
        [{"type": "bar"}, {"type": "pie"}],  # First row
        [{"type": "scatter", "colspan": 2}, None]  # Second row (span 2 columns)
    ],
    subplot_titles=(  # Titles for each subplot
        "Monthly Sales Performance", 
        "Product Mix", 
        "Daily Sales Trend"
    )
)

# ----------------------
# Chart 1: Bar Chart (Monthly Sales/Expenses)
# ----------------------

# Add sales bar chart
fig.add_trace(
    go.Bar(
        x=months,  # X-axis values
        y=sales,  # Y-axis values
        name="Sales",  # Legend label
        marker_color='#636EFA',  # Blue color
        text=[f'₹{x:,.0f}' for x in sales],  # Bar labels
        textposition='auto'  # Automatic label positioning
    ),
    row=1, col=1  # Position in subplot grid
)

# Add expenses bar chart
fig.add_trace(
    go.Bar(
        x=months,
        y=expenses,
        name="Expenses",
        marker_color='#EF553B',  # Red color
        text=[f'₹{x:,.0f}' for x in expenses],
        textposition='auto'
    ),
    row=1, col=1
)

# ----------------------
# Chart 2: Pie Chart (Product Mix)
# ----------------------

fig.add_trace(
    go.Pie(
        labels=products,  # Product names
        values=product_sales,  # Sales values
        name="Product Sales",
        marker_colors=['#00CC96', '#AB63FA', '#FFA15A'],  # Custom colors
        hole=0.4,  # Donut hole size
        hoverinfo="label+percent+value",  # Hover content
        textinfo="value"  # Show values on chart
    ),
    row=1, col=2
)

# ----------------------
# Chart 3: Line Chart (Daily Trend)
# ----------------------

fig.add_trace(
    go.Scatter(
        x=date_range,  # Dates on x-axis
        y=daily_sales,  # Sales values
        mode='lines+markers',  # Show both lines and markers
        name="Daily Sales",
        line=dict(color='#19D3F3', width=3),  # Line styling
        marker=dict(size=8),  # Marker size
        fill='tozeroy',  # Fill below line
        fillcolor='rgba(25, 211, 243, 0.2)'  # Fill color with transparency
    ),
    row=2, col=1
)

# ======================
# 3. STYLING & LAYOUT
# ======================

fig.update_layout(
    title={
        'text': f"<b>Sales Dashboard</b><br><sup>Generated on {datetime.now().strftime('%Y-%m-%d')}</sup>",
        'x':0.5,  # Center title
        'font': {'size': 24}  # Title font size
    },
    showlegend=True,  # Show legend
    hovermode="x unified",  # Unified hover across subplots
    plot_bgcolor='rgba(240,240,240,0.8)',  # Plot background
    paper_bgcolor='rgba(240,240,240,1)',  # Overall background
    height=800,  # Figure height
    annotations=[  # Additional annotations
        dict(
            text="All values in ₹ (INR)",
            x=0, y=1.1,  # Position above top
            xref="paper", yref="paper",  # Relative coordinates
            showarrow=False  # No arrow
        )
    ]
)

# Format x-axes
fig.update_xaxes(
    showgrid=True,  # Show grid lines
    gridwidth=0.5,  # Grid line width
    gridcolor='lightgray'  # Grid color
)

# Format y-axes
fig.update_yaxes(
    showgrid=True,
    gridwidth=0.5,
    gridcolor='lightgray',
    tickprefix="₹",  # Currency prefix
    tickformat=",.0f"  # Thousands separator
)

# ======================
# 4. ADD INTERACTIVE CONTROLS
# ======================

fig.update_layout(
    updatemenus=[  # Add interactive buttons
        dict(
            type="buttons",  # Button type
            direction="right",  # Button arrangement
            x=1, y=1.15,  # Position (right-top)
            buttons=list([
                dict(
                    label="Reset View",  # Button label
                    method="relayout",  # Action type
                    args=[{"xaxis.range": None, "yaxis.range": None}]  # Reset zoom
                ),
                dict(
                    label="Zoom to Q1",
                    method="relayout",
                    args=[{"xaxis.range": [0, 2]}]  # Zoom to first 3 months
                )
            ])
        )
    ]
)

# ======================
# 5. DISPLAY & SAVE
# ======================

fig.show()  # Display in browser/notebook

# Save as interactive HTML (uncomment to use)
# fig.write_html("sales_dashboard.html")
