// const APIKEY = "9FQR18B2ELUY5F27";
const getstockdata = async (symbol) => {
    const response = await fetch('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol='+symbol+'&apikey=demo');
    const data = await response.json();
    return data;
}


const formatstockdata = (data,cnt) => {
    const weeklydata = data['Weekly Adjusted Time Series'];
    console.log(typeof(weeklydata));
    const stockdata = [];
    let count = 0;
    const volume = [];
    for (let key in weeklydata) {
        count++;
        if(count>cnt)break;
        const stock = {
            x: key,
            y: [weeklydata[key]['1. open'], weeklydata[key]['2. high'], weeklydata[key]['3. low'], weeklydata[key]['4. close']]
        }
        stockdata.push(stock);
        //if loss negative volume
        const vol = {
            x: key,
            y: weeklydata[key]['6. volume']
        }
        volume.push(vol);
        
    }
    return [stockdata,volume];
}
export { getstockdata ,formatstockdata};