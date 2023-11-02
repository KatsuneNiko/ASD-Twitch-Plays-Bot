import React from "react";
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";
import * as RiIcons from "react-icons/ri";
 
export const SidebarData = [
  {
    title: "Home",
    path: "/",
    icon: <AiIcons.AiFillHome />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,
 
    subNav: [
      {
        title: "Introduction",
        path: "/Introduction",
        icon: <IoIcons.IoIosPaper />,
      },
      {
        title: "Help",
        path: "/Help",
        icon: <IoIcons.IoIosPaper />,
      },
    ],
  },

  {
    title: "CRUD Keyboard",
    path: "/CRUDKeyboard",
    icon: <FaIcons.FaKeyboard />,
  },

  {
    title: "CRUD Mouse",
    path: "/CRUDMouse",
    icon: <FaIcons.FaMouse />,
  },

  {
    title: "Statistics",
    path: "/Statistics",
    icon: <FaIcons.FaPercent />,
  },

  {
    title: "Select Profile",
    path: "/SelectProfile",
    icon: <FaIcons.FaUser />,
  },

  {
    title: "Style of Play",
    path: "/StyleOfPlay",
    icon: <FaIcons.FaGamepad />,
  },

  {
    title: "Chatbot on Discord",
    path: "/ChatbotOnDiscord",
    icon: <FaIcons.FaDiscord />,
  },

  {
    title: "Split Mode",
    path: "/SplitMode",
    icon: <FaIcons.FaSplotch />,
  },

  {
    title: "Valid Keyword",
    path: "/ValidKeyword",
    icon: <FaIcons.FaTable/>,
  },
];