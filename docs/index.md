每月租金

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "Stock prices of 5 Tech Companies over Time.",
  "data": {"url": "assets/data/2.csv"},
  "height": "300",
  "mark": {"type": "line", "point": true, "tooltip": true},
  "encoding": {
    "x": {"timeUnit": "month", "field": "month"},
    "y": {"field": "mean", "type": "quantitative"},
    "color": {"field": "district", "type": "nominal"}
  }
}
```