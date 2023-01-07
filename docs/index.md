每月租金

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "A simple bar chart with embedded data.",
  "data": {"url" : "assets/data/1.json"},
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "y": {
      "field": "district",
      "type": "nominal",
      "axis": {"labelAngle": 0},
      "sort": {"field": "median_rental_by_month"}
    },
    "x": {"field": "median_rental_by_month", "type": "quantitative"}
  }
}
```