import React from 'react'
import { useState,useEffect,useRef } from 'react'
import { getstockdata,formatstockdata } from './data/service.js'
import {candlestickoptions,baroptions} from './data/options.js'
import Loading from './Loading.jsx'
import Chart from "react-apexcharts";



function Livechart({symbol}) {
    const count = useRef(40);
    const [viewcandledata, setviewcandledata] = useState([]);
    const [volumedata, setvolumedata] = useState([]);
    const [loading, setloading] = useState(true);
    useEffect(() => {
        setloading(true);
        getstockdata(symbol).then((data) => {
            const [stock,volume] = formatstockdata(data,200);
            setviewcandledata(stock);
            setvolumedata(volume);
            setloading(false);
        });
       
    }
    ,[symbol]);
    useEffect(() => {
        const interval = setInterval(() => {
            setviewcandledata(viewcandledata.slice(0,count.current));
            setvolumedata(volumedata.slice(0,count.current));
            count.current++;
            setloading(false);
        }, 10000);
        return () => clearInterval(interval);
    }
    ,[symbol,viewcandledata,volumedata]);
  return (
    (loading?<Loading/>:
    <>
    <Chart className="bg-white border p-2 m-2 border-gray-200 rounded-lg shadow-xl"
        options={candlestickoptions}
        series={[{data:viewcandledata}]}
        type="candlestick"
        width={1000}
        height={500}
    />
    <Chart className="bg-white border p-2 m-2 border-gray-200 rounded-lg shadow-xl"
        options={baroptions}
        series={[{data:volumedata}]}
        type="bar"
        width={1000}
        height={200}
        />
    </>
    )

  )
}

export default Livechart