const Tab = ({ name, onClick }) => {
    return (
        <div className="rounded-t-md px-4 bg-black py-2 flex justify-between gap-x-12">
            <div className="text-sm text-orange">
                { name }
            </div>
            <button className="text-ocean text-sm" type="button" onClick={onClick}>
                X
            </button>
        </div>
    )
}

const TabLine = ({ notes, removeNote }) => {
    return (
        <div className="flex jusitfy-start items-end ml-10 gap-x-3">
            {
                notes?.map(value => (
                    <Tab name={value.title} onClick={() => removeNote(value.id)} key={value.id}/>
                ))
            }
            <button className="text-xl text-white ml-2 mb-1" type="button"> 
                +
            </button>
        </div>
    )
};

export default TabLine;