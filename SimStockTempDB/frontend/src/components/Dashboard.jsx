import React from 'react';
import Livechart from './Livechart.jsx';
import { useState,useEffect } from 'react';
import Companylist from './Companylist.jsx';

function Dashboard(props) {
    const [companysymbol, setcompanysymbol] = useState('IBM');
    return (
        <>
            <div className='flex'>
                <div className="flex-1 flex items-center justify-center flex-col w-5/6 "><Livechart  symbol={companysymbol} setsymbol={setcompanysymbol}/></div>
                <div className="flex-initial w-1/6"><Companylist symbol={companysymbol} setsymbol={setcompanysymbol}/></div>
            </div>
        </>
    );
}
export default Dashboard;