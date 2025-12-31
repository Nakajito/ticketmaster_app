import {Fragment,useCallback,useContext,useEffect} from "react"
import {Badge as RadixThemesBadge,Box as RadixThemesBox,Button as RadixThemesButton,Callout as RadixThemesCallout,Card as RadixThemesCard,Container as RadixThemesContainer,Flex as RadixThemesFlex,Grid as RadixThemesGrid,Heading as RadixThemesHeading,Inset as RadixThemesInset,Link as RadixThemesLink,Select as RadixThemesSelect,Separator as RadixThemesSeparator,Text as RadixThemesText,TextField as RadixThemesTextField} from "@radix-ui/themes"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent,isTrue} from "$/utils/state"
import {Search as LucideSearch,TriangleAlert as LucideTriangleAlert} from "lucide-react"
import {Link as ReactRouterLink} from "react-router"
import {jsx} from "@emotion/react"




function Textfield__root_8417ee685524e339d70f75bca59395f7 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_d45241e65405381af35d2f3f85018599 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ticketmaster_app___ticketmaster_app____state.handle_search_change", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesTextField.Root,{css:({ ["@media screen and (min-width: 0)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 30em)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 48em)"] : ({ ["width"] : "250px" }) }),onChange:on_change_d45241e65405381af35d2f3f85018599,placeholder:"Artista o evento..."},)
  )
}


function Select__root_3f41631ff4eab272469e509e3e287e4a () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_2f7235af1fa884294ad7262ac90b1405 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ticketmaster_app___ticketmaster_app____state.set_city_filter", ({ ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{defaultValue:"Todas las ciudades",onValueChange:on_change_2f7235af1fa884294ad7262ac90b1405},jsx(RadixThemesSelect.Trigger,{css:({ ["@media screen and (min-width: 0)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 30em)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 48em)"] : ({ ["width"] : "200px" }) }),placeholder:"Selecciona Ciudad"},),jsx(RadixThemesSelect.Content,{},jsx(RadixThemesSelect.Group,{},"",jsx(RadixThemesSelect.Item,{value:"Todas las ciudades"},"Todas las ciudades"),jsx(RadixThemesSelect.Item,{value:"Ciudad de Mexico"},"Ciudad de Mexico"),jsx(RadixThemesSelect.Item,{value:"Monterrey"},"Monterrey"),jsx(RadixThemesSelect.Item,{value:"Guadalajara"},"Guadalajara"))))
  )
}


function Select__root_add40f8ca3684acf0c59e35412a7e07e () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_a9887f73f41a61dbd927f6468657082b = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ticketmaster_app___ticketmaster_app____state.set_category_filter", ({ ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{onValueChange:on_change_a9887f73f41a61dbd927f6468657082b},jsx(RadixThemesSelect.Trigger,{css:({ ["@media screen and (min-width: 0)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 30em)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 48em)"] : ({ ["width"] : "180px" }) }),placeholder:"Categor\u00eda"},),jsx(RadixThemesSelect.Content,{},jsx(RadixThemesSelect.Group,{},"",jsx(RadixThemesSelect.Item,{value:"Todas"},"Todas"),jsx(RadixThemesSelect.Item,{value:"Music"},"Music"),jsx(RadixThemesSelect.Item,{value:"Sports"},"Sports"),jsx(RadixThemesSelect.Item,{value:"Arts & Theatre"},"Arts & Theatre"),jsx(RadixThemesSelect.Item,{value:"Family"},"Family"))))
  )
}


function Button_0a19b40f364b29b8fa52069caa10048b () {
  const reflex___state____state__ticketmaster_app___ticketmaster_app____state = useContext(StateContexts.reflex___state____state__ticketmaster_app___ticketmaster_app____state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_f2bf2295ec15c5584cde5d4d9df39ae0 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ticketmaster_app___ticketmaster_app____state.search_events", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["@media screen and (min-width: 0)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 30em)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 48em)"] : ({ ["width"] : "auto" }) }),loading:reflex___state____state__ticketmaster_app___ticketmaster_app____state.is_loading_rx_state_,onClick:on_click_f2bf2295ec15c5584cde5d4d9df39ae0},jsx(LucideSearch,{},),"Buscar")
  )
}


function Callout__text_c978339733d06df3d2bbe2c5491aacee () {
  const reflex___state____state__ticketmaster_app___ticketmaster_app____state = useContext(StateContexts.reflex___state____state__ticketmaster_app___ticketmaster_app____state)



  return (
    jsx(RadixThemesCallout.Text,{},reflex___state____state__ticketmaster_app___ticketmaster_app____state.error_message_rx_state_)
  )
}


function Fragment_9b644a4e5690bfe38c711c565dbcb4f4 () {
  const reflex___state____state__ticketmaster_app___ticketmaster_app____state = useContext(StateContexts.reflex___state____state__ticketmaster_app___ticketmaster_app____state)



  return (
    jsx(Fragment,{},(!((reflex___state____state__ticketmaster_app___ticketmaster_app____state.error_message_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesCallout.Root,{color:"red",css:({ ["icon"] : "triangle_alert" })},jsx(RadixThemesCallout.Icon,{},jsx(LucideTriangleAlert,{},)),jsx(Callout__text_c978339733d06df3d2bbe2c5491aacee,{},)))):(jsx(Fragment,{},))))
  )
}


function Grid_272b66d16201cf5f77fc172b561ecc18 () {
  const reflex___state____state__ticketmaster_app___ticketmaster_app____state = useContext(StateContexts.reflex___state____state__ticketmaster_app___ticketmaster_app____state)



  return (
    jsx(RadixThemesGrid,{columns:({ ["initial"] : "1", ["sm"] : "2", ["md"] : "3", ["lg"] : "4" }),css:({ ["width"] : "100%" }),gap:"4"},Array.prototype.map.call(reflex___state____state__ticketmaster_app___ticketmaster_app____state.events_rx_state_ ?? [],((event_rx_state_,index_9fbe54e4dd9f60b27ef75ed8399b8f5c)=>(jsx(RadixThemesCard,{css:({ ["width"] : "100%" }),key:index_9fbe54e4dd9f60b27ef75ed8399b8f5c},jsx(RadixThemesInset,{pb:"current",side:"top"},jsx("img",{css:({ ["width"] : "100%", ["height"] : "150px", ["objectFit"] : "cover" }),src:event_rx_state_?.["image"]},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"2"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",gap:"3"},jsx(RadixThemesBadge,{color:"violet",variant:"soft"},event_rx_state_?.["date"]),jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},),jsx(RadixThemesBadge,{color:event_rx_state_?.["status_color"],variant:"solid"},event_rx_state_?.["status"])),jsx(RadixThemesHeading,{size:"3",trim:"both"},event_rx_state_?.["name"]),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray" }),size:"1"},event_rx_state_?.["venue"]),jsx(RadixThemesText,{as:"p",size:"2",weight:"bold"},event_rx_state_?.["price"]),jsx(RadixThemesLink,{asChild:true,css:({ ["width"] : "100%", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{target:(true ? "_blank" : ""),to:event_rx_state_?.["url"]},jsx(RadixThemesButton,{css:({ ["width"] : "100%", ["cursor"] : "pointer" }),variant:"surface"},"Ir a Ticketmaster")))))))))
  )
}


function Button_76aabf57dd2fbefaac9f17e8d701fb75 () {
  const reflex___state____state__ticketmaster_app___ticketmaster_app____state = useContext(StateContexts.reflex___state____state__ticketmaster_app___ticketmaster_app____state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_5065f7844530bd4a0c546898fd801818 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ticketmaster_app___ticketmaster_app____state.prev_page", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{disabled:(reflex___state____state__ticketmaster_app___ticketmaster_app____state.page_rx_state_?.valueOf?.() === 0?.valueOf?.()),onClick:on_click_5065f7844530bd4a0c546898fd801818,variant:"soft"},"Anterior")
  )
}


function Text_d90c1d2fdb2895cc69f455ce10ab3417 () {
  const reflex___state____state__ticketmaster_app___ticketmaster_app____state = useContext(StateContexts.reflex___state____state__ticketmaster_app___ticketmaster_app____state)



  return (
    jsx(RadixThemesText,{as:"p",weight:"bold"},("P\u00e1gina "+(reflex___state____state__ticketmaster_app___ticketmaster_app____state.page_rx_state_ + 1)))
  )
}


function Button_57d7d5c03cd6cce5791117b241894e29 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_14075eb1c7c97e4250384b833f4d8795 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ticketmaster_app___ticketmaster_app____state.next_page", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{onClick:on_click_14075eb1c7c97e4250384b833f4d8795,variant:"soft"},"Siguiente")
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesContainer,{css:({ ["padding"] : "16px" }),size:"3"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["paddingTop"] : "4em", ["paddingBottom"] : "4em" }),direction:"column",gap:"3"},jsx(RadixThemesBox,{},jsx(RadixThemesHeading,{css:({ ["marginBottom"] : "0.5em" }),size:"9"},"\ud83c\udfab EventFinder M\u00e9xico \ud83c\udfab"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "gray", ["marginBottom"] : "1.5em", ["textAlign"] : "center" })},"Encuentra los mejores eventos en tu ciudad.")),jsx(RadixThemesFlex,{css:({ ["flexWrap"] : "wrap", ["width"] : "100%" }),justify:"center",gap:"3"},jsx(Textfield__root_8417ee685524e339d70f75bca59395f7,{},),jsx(Select__root_3f41631ff4eab272469e509e3e287e4a,{},),jsx(Select__root_add40f8ca3684acf0c59e35412a7e07e,{},),jsx(Button_0a19b40f364b29b8fa52069caa10048b,{},)),jsx(Fragment_9b644a4e5690bfe38c711c565dbcb4f4,{},),jsx(RadixThemesSeparator,{css:({ ["marginTop"] : "2em", ["marginBottom"] : "2em" }),size:"4"},),jsx(Grid_272b66d16201cf5f77fc172b561ecc18,{},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["marginTop"] : "2em", ["width"] : "100%" }),direction:"row",justify:"center",gap:"4"},jsx(Button_76aabf57dd2fbefaac9f17e8d701fb75,{},),jsx(Text_d90c1d2fdb2895cc69f455ce10ab3417,{},),jsx(Button_57d7d5c03cd6cce5791117b241894e29,{},)))),jsx("title",{},"EventFinder MX"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}