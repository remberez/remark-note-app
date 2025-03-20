const Tab = ({ name }) => {
    return (
        <div className="rounded-t-md px-4 bg-black py-2 flex justify-between gap-x-12">
            <div className="text-sm text-orange">
                { name }
            </div>
            <button className="text-ocean text-sm" type="button">
                X
            </button>
        </div>
    )
}

const TabLine = () => {
    return (
        <div className="flex jusitfy-start items-end ml-10 gap-x-3">
            <Tab name="Первая заметка"/>
            <Tab name="Первая заметка"/>
            <button className="text-xl text-white ml-2 mb-1" type="buttonm"> 
                +
            </button>
        </div>
    )
};

export default TabLine;