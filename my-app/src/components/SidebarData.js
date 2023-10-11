import React from "react";
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";
import * as RiIcons from "react-icons/ri";
 
export const SidebarData = [
  {
    title: "Home",
    path: "/pages/Home",
    icon: <AiIcons.AiFillHome />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,
 
    subNav: [
      {
        title: "Introduction",
        path: "/Home/Introduction",
        icon: <IoIcons.IoIosPaper />,
      },
      {
        title: "Help",
        path: "/Home/Help",
        icon: <IoIcons.IoIosPaper />,
      },
    ],
  },

  {
    title: "Marcos",
    path: "/Marcos",
    icon: <FaIcons.FaKeyboard />,
  },

  {
    title: "Participation Setting",
    path: "/Participation",
    icon: <FaIcons.FaSmile />,
  },

  {
    title: "Statistics",
    path: "/Statistics",
    icon: <FaIcons.FaPercent />,
  },

  {
    title: "Account Setting",
    path: "/AccountSetting",
    icon: <IoIcons.IoMdHelpCircle />,
  },
  {
    title: "Mouse Macro",
    path: "/MouseMacro",
    icon: <FaIcons.FaMouse />,
  }
];