import React from 'react'
import companies from './data/companieslist'

function Companylist({symbol,setsymbol}) {
  return (
    <div>    
        <select id="underline_select" onClick={(event)=>{setsymbol(event.target.value)}} className="block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer">
            {companies.map((company) => (
                <option value={company.symbol} selected={company.symbol===symbol}>{company.name}</option>
            ))}
        </select>
        
        
        
            
    </div>

  )
}

export default Companylist