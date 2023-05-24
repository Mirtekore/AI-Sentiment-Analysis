import React, {useEffect, useState} from 'react';
import ReactECharts from 'echarts-for-react';
import { styled } from '@mui/material/styles';
import colors from 'src/utils/colorSeries';
import { Card, CardHeader, Select, MenuItem, InputLabel, FormControl } from '@mui/material';

const CHART_HEIGHT = 400;
const LEGEND_HEIGHT = 72;

const ChartWrapperStyle = styled('div')(({ theme }) => ({
  height: CHART_HEIGHT,
  marginTop: theme.spacing(2),
  '& .apexcharts-canvas svg': {
    height: CHART_HEIGHT
  },
  '& .apexcharts-canvas svg,.apexcharts-canvas foreignObject': {
    overflow: 'visible',
  },
  '& .apexcharts-legend': {
    height: LEGEND_HEIGHT,
    alignContent: 'center',
    position: 'relative !important',
    borderTop: `solid 1px ${theme.palette.divider}`,
    top: `calc(${CHART_HEIGHT - LEGEND_HEIGHT}px) !important`
  }
}));

var headers = new Headers({
  'Authorization': `Basic ${btoa("admin" + ':' + "Zi12ZnK2r2n")}`
});

const CHART_DATA = [];    

export default function PieChart() {
  const [chartData, setChartData ] = useState([]);

  useEffect(() => {
    fetch('http://172.26.135.240:5984/mast/_design/mastview/_view/sentiment?group=true',
      {headers: {
        'Authorization': 'Basic ' + btoa('admin:Zi12ZnK2r2n')
      }, method: 'GET',
    }).then(
      response => response.json()
    ).then(
      data => {
        let chartData = [];     
        data['rows'].forEach(item => {
          const key = item.key;
          const value = item.value;
          chartData.push({value: value, name: key});
        });

        setChartData(chartData);     
       }
    );
  }, []);

  const options = {
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',
      left: 20
    },
    series: [
      {
        // name: 'Access From',
        type: 'pie',
        radius: '70%',
        center: ['55%', '60%'],
        color: colors,
        data: chartData,
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }, 
      }
    ]    
  };


  return (
    <Card>
      <CardHeader title="Twitter Sentiments" />
        <ChartWrapperStyle dir="ltr">
        <ReactECharts option={options} sytle={{height: 300}}/>
        </ChartWrapperStyle>
        {/* <FormControl
          sx={{ m:1, minWidth: 120, marginLeft: "40%"}}
        >
          <InputLabel id="aspect-select">indicator</InputLabel>
          <Select
              label="indicator"
              value={indicator}
              onChange={e=>{setIndicator(e.target.value)}}
              style={{ width:200, height:40, marginLeft:"1%", marginBottom: 20 }}
          >
            { fields.map(item => (
              <MenuItem value={item}>{item}</MenuItem>
            ))}
          </Select>
        </FormControl> */}
    </Card>
  )
}