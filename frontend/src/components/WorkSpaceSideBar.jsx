import { RiStickyNoteAddLine } from "react-icons/ri";
import { FaFolderPlus } from "react-icons/fa";
import { FaSortAmountDownAlt } from "react-icons/fa";
import { Link } from "react-router-dom";

const SideBar = () => {
    return (
        <aside className="flex bg-lightGray">
            <div className="w-[70px] border-r-2 border-veryLightGray">
                
            </div>
            <div className="border-r-2 border-veryLightGray w-full pl-4 pt-4">
                <div className="flex justify-start items-start gap-x-5">
                    <button>
                        <RiStickyNoteAddLine fill="white" size="20"/>
                    </button>
                    <button>
                        <FaFolderPlus fill="white" size="20"/>
                    </button>
                    <button>
                        <FaSortAmountDownAlt fill="white" size="20"/>         
                    </button>
                </div>
                <ul className="text-white flex flex-col gap-y-4 mt-4">
                    <li>
                        <Link>
                            Первая заметка
                        </Link>
                    </li>
                    <li>
                        <Link>
                            Вторая заметка
                        </Link>
                    </li>
                </ul>
            </div>
        </aside>
    )
}

export default SideBar;