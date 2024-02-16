
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv






<!DOCTYPE html>
<html lang="en">

<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no,user-scalable=no"><meta name="theme-color" content="#FFFFFF"><link rel="mask-icon" href="/-/build/favicon_safari_mask.png" color="#FF2B2B"><link rel="apple-touch-icon" href="/-/build/favicon_256.png"><link rel="manifest" href="/-/build/manifest.json"><script src="https://js.hs-banner.com/v2/6571207/banner.js" type="text/javascript" id="cookieBanner-6571207" data-cookieconsent="ignore" data-hs-ignore="true" data-loader="hs-scriptloader" data-hsjs-portal="6571207" data-hsjs-env="prod" data-hsjs-hublet="na1"></script><script type="text/javascript" data-cfasync="false" charset="UTF-8" async="" src="https://cdn.heapanalytics.com/js/replay/libs/latest/auryc.lib.js"></script><script src="https://js-na1.hs-scripts.com/6571207.js" type="text/javascript" id="hs-script-loader"></script><script type="text/javascript" async="" src="https://cdn.heapanalytics.com/js/heap-269788835.js"></script><script type="text/javascript" async="" src="https://js.hs-analytics.net/analytics/1708074300000/6571207.js" id="hs-analytics"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script type="text/javascript" src="https://cdn.segment.com/next-integrations/integrations/vendor/commons.c42222c4cb2f8913500f.js.gz" async="" status="loaded"></script><script type="text/javascript" src="https://cdn.segment.com/next-integrations/integrations/heap/2.1.2/heap.dynamic.js.gz" async="" status="loaded"></script><script type="text/javascript" src="https://cdn.segment.com/next-integrations/integrations/hubspot/2.2.4/hubspot.dynamic.js.gz" async="" status="loaded"></script><script type="text/javascript" async="" src="https://cdn.segment.com/analytics.js/v1/GI7vYWHNmWwHbyFjBrvL0jOBA1TpZOXC/analytics.min.js"></script><script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-52GRQSL"></script><script>!function(e,t,a,n,g){e[n]=e[n]||[],e[n].push({"gtm.start":(new Date).getTime(),event:"gtm.js"});var m=t.getElementsByTagName(a)[0],r=t.createElement(a);r.async=!0,r.src="https://www.googletagmanager.com/gtm.js?id=GTM-52GRQSL",m.parentNode.insertBefore(r,m)}(window,document,"script","dataLayer")</script><script>!function(){var e=window.analytics=window.analytics||[];if(!e.initialize)if(e.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{e.invoked=!0,e.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","debug","page","once","off","on","addSourceMiddleware","addIntegrationMiddleware","setAnonymousId","addDestinationMiddleware"],e.factory=function(t){return function(){var n=Array.prototype.slice.call(arguments);return n.unshift(t),e.push(n),e}};for(var t=0;t<e.methods.length;t++){var n=e.methods[t];e[n]=e.factory(n)}e.load=function(t,n){var a=document.createElement("script");a.type="text/javascript",a.async=!0,a.src="https://cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var r=document.getElementsByTagName("script")[0];r.parentNode.insertBefore(a,r),e._loadOptions=n},e.SNIPPET_VERSION="4.13.1",e.load("GI7vYWHNmWwHbyFjBrvL0jOBA1TpZOXC")}}()</script><script defer="defer" src="/-/build/static/js/main.9f19a037.js"></script><link href="/-/build/static/css/main.2b833414.css" rel="stylesheet"><style data-dynamic-styles-ar="">/** arPreserve @keyframes st-ae {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}.st-ae { display: block; }.st-af { animation-name: st-ae; }.st-ag { animation-duration: 1000ms; }.st-ah { animation-iteration-count: infinite; }.st-ai { animation-timing-function: linear; }.st-aj { border-left-style: solid; }.st-ak { border-right-style: solid; }.st-al { border-top-style: solid; }.st-am { border-bottom-style: solid; }.st-an { border-radius: 50%; }.st-ao { border-top-color: rgb(28, 131, 225); }.st-ap { border-right-color: rgb(238, 238, 238); }.st-aq { border-bottom-color: rgb(238, 238, 238); }.st-ar { border-left-color: rgb(238, 238, 238); }.st-as { border-left-width: 4px; }.st-at { border-right-width: 4px; }.st-au { border-top-width: 4px; }.st-av { border-bottom-width: 4px; }.st-aw { width: 32px; }.st-ax { height: 32px; }.st-ay { cursor: wait; }html > x-root-ktbk4#pb_rl61mm5jrh5 { background: none !important; border: 0px !important; border-radius: 0px !important; left: -16px !important; top: -16px !important; right: initial !important; bottom: initial !important; width: 16px !important; height: 16px !important; margin: 0px !important; padding: 0px !important; position: absolute !important; transform: none !important; z-index: 2147483647 !important; box-shadow: none !important; filter: none !important; transition: none 0s ease 0s !important; overflow: visible !important; outline: none !important; visibility: hidden !important; }html > x-root-ktbk4#pb_rl61mm5jrh5[pseudo], html > x-root-ktbk4#pb_rl61mm5jrh5::before, html > x-root-ktbk4#pb_rl61mm5jrh5::after, html > x-root-ktbk4#pb_rl61mm5jrh5::before, html > x-root-ktbk4#pb_rl61mm5jrh5::after, html > x-root-ktbk4#pb_rl61mm5jrh5 > x-icon-o3bfq::before, html > x-root-ktbk4#pb_rl61mm5jrh5 > x-icon-o3bfq::after, html > x-root-ktbk4#pb_rl61mm5jrh5 > x-icon-o3bfq::before, html > x-root-ktbk4#pb_rl61mm5jrh5 > x-icon-o3bfq::after, html > x-root-ktbk4#pb_rl61mm5jrh5 > [x-icon-o3bfq]::before, html > x-root-ktbk4#pb_rl61mm5jrh5 > [x-icon-o3bfq]::after, html > x-root-ktbk4#pb_rl61mm5jrh5 > [x-icon-o3bfq]::before, html > x-root-ktbk4#pb_rl61mm5jrh5 > [x-icon-o3bfq]::after { display: none !important; }html > x-root-ktbk4#pb_rl61mm5jrh5 > x-icon-o3bfq { background: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/Pgo8c3ZnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgaGVpZ2h0PSIxNiIgd2luZHRoPSIxMDI0IiB3aWR0aD0iMTYiPgogIDxwYXRoIGQ9Ik03NjcuMDgzIDc1OC4xNDRDODk5LjA5NCA1MzIuMjg4IDk2OS44NTYgMjczLjk2MyA5NjkuODU2IDcuNjM3aC02MC44ODVWOTMuMjlDODAyLjI0IDM0LjA2OSA2ODIuNTM5IDIuOTIyIDU2MC4wNjQgMi45MjJjLTExNy4wOTkgMC0yMzEuNzg3IDI5LjA1Ni0zMzQuNTQ5IDg0LjMzMVY3LjYzN2gtNjAuNjA4YzAgMjY2LjMyNSA3MC43NjMgNTI0LjY1MSAyMDIuNzczIDc1MC41MDdoLTYzLjM4MWMtMTMuNTY4LTY4LjEzOS03My40NzItMTE5LjYxNi0xNDUuMTUyLTExOS42MTYtODEuNjY0IDAtMTQ4LjA3NSA2Ni44MTYtMTQ4LjA3NSAxNDguOTA3czY2LjQzMiAxNDguOTA3IDE0OC4wNzUgMTQ4LjkwN2M3MS42OCAwIDEzMS41ODQtNTEuNDk5IDE0NS4xNTItMTE5LjYxNmg5OS41MmExNDg4Ljk0IDE0ODguOTQgMCAwIDAgMTQxLjk1MiAxODUuMjE2bDIxLjYxMSAyNCAyMS42MTEtMjRhMTQ4NS4zNDcgMTQ4NS4zNDcgMCAwIDAgMTQxLjk3My0xODUuMjE2aDEwNi4xNzZ2MTAyLjI3Mmg1OC4yNFY4MTYuNzI2aDYzLjIzMnYxMDIuMjcyaDU4LjI4M1Y3NTguMTQ1SDc2Ny4wODR6TTE1OS4xNDcgODc3LjczOWMtNDkuNTE1IDAtODkuNzkyLTQwLjUxMi04OS43OTItOTAuMjgzIDAtNDkuNzkyIDQwLjI3Ny05MC4yNjEgODkuNzkyLTkwLjI2MSA0OS40OTMgMCA4OS43NzEgNDAuNDY5IDg5Ljc3MSA5MC4yNjEuMDIxIDQ5Ljc0OS00MC4yNTYgOTAuMjgzLTg5Ljc3MSA5MC4yODN6bTEyMS41NzgtNTIwLjA2NGMwLTcxLjM4MSA1Ny43NzEtMTI5LjQ3MiAxMjguNzQ3LTEyOS40NzIgNzEuMDE5IDAgMTI4Ljc0NyA1OC4wOTEgMTI4Ljc0NyAxMjkuNDcydjczLjM0NGg1OC4zMDR2LTczLjM0NGMwLTcxLjM4MSA1Ny43MjgtMTI5LjQ3MiAxMjguNzQ3LTEyOS40NzIgNzAuOTk3IDAgMTI4Ljc0NyA1OC4wOTEgMTI4Ljc0NyAxMjkuNDcyIDAgMTYwLjkxNy0xMjguNTk3IDI5MS44NC0yODYuNjc3IDI5MS44NC0xNTguMDE2IDAtMjg2LjYxMy0xMzAuOTAxLTI4Ni42MTMtMjkxLjg0em0yNzkuMzE4LTI5Ni4xNWMxMjEuNDcyIDAgMjM5Ljg3MiAzMy4zMjMgMzQzLjU1MiA5Ni4zODQtMy43NTUgMzYuMTYtOC45MzkgNzIuMDY0LTE1LjQyNCAxMDcuNjI3LTMyLjEyOC01Ny4xOTUtOTMuMDU2LTk1Ljk1Ny0xNjIuOTAxLTk1Ljk1Ny02Ni40MzIgMC0xMjQuNzM2IDM1LjA5My0xNTcuOTA5IDg3LjcwMS0zMy4xNzMtNTIuNjA4LTkxLjQ3Ny04Ny43MDEtMTU3Ljg4OC04Ny43MDEtNjkuODAzIDAtMTMwLjcwOSAzOC43NDEtMTYyLjg1OSA5NS44OTMtNi44NDgtMzcuNjExLTEyLjI2Ny03NS41NjMtMTYuMDg1LTExMy43OTIgOTkuOTA0LTU5LjAwOCAyMTMuNDE5LTkwLjE1NSAzMjkuNTE1LTkwLjE1NXpNMzc0LjM3OSA2NDhjNTUuMTA0IDM3Ljk1MiAxMjEuNTU3IDYwLjEzOSAxOTMuMDAzIDYwLjEzOSA3MS40ODggMCAxMzcuOTYzLTIyLjE4NyAxOTMuMDY3LTYwLjE2LTE4Ljc5NSAzNy41NjgtMzkuMzM5IDc0LjI4My02MS40ODMgMTEwLjE2NUg0MzUuNzk4QTE0MTguOTMyIDE0MTguOTMyIDAgMCAxIDM3NC4zNzkgNjQ4em0xOTMuMDAyIDI5MC4wMjdjLTMzLjM4Ny0zOC44NjktNjQuNDkxLTc5LjQwMy05My4zMTItMTIxLjMwMWgxODYuNjY3Yy0yOC44MjEgNDEuODk5LTU5LjkyNSA4Mi40MTEtOTMuMzU1IDEyMS4zMDF6TTQwOS40NzIgMzAzLjI1M2MtMjkuODg4IDAtNTQuMTIzIDI0LjM4NC01NC4xMjMgNTQuNDIxIDAgNy4xODkgMS40NzIgMTQuMDM3IDMuOTg5IDIwLjMwOSA0MS42MjEtMjQuNDQ4IDc4LjU0OS0yLjk0NCA5NS4wNjEgMTAuMDQ4YTU0LjQzMyA1NC40MzMgMCAwIDAgOS4xOTUtMzAuMzU3YzAtMzAuMDM3LTI0LjIxMy01NC40MjEtNTQuMTIzLTU0LjQyMXptMzY2LjQgNzMuMzIzYzIuMTc2LTUuOTA5IDMuNTQxLTEyLjIwMyAzLjU0MS0xOC45MDEgMC0zMC4wMzctMjQuMjM1LTU0LjQyMS01NC4xMDEtNTQuNDIxLTI5LjkzMSAwLTU0LjE2NSAyNC4zODQtNTQuMTY1IDU0LjQyMSAwIDExLjkwNCAzLjkwNCAyMi44MDUgMTAuMzQ3IDMxLjc2NSAxNS4yMzItMTIuNDggNTIuMjQ1LTM1Ljg4MyA5NC4zNzktMTIuODY0eiIgc3R5bGU9ImZpbGw6ICM3NjgzODc7Ii8+Cjwvc3ZnPg==") center center / 16px 16px no-repeat !important; border: 0px !important; border-radius: 0px !important; left: -16px !important; top: -16px !important; right: initial !important; bottom: initial !important; margin: 0px !important; padding: 0px !important; position: absolute !important; transform: none !important; z-index: 2147483647 !important; box-shadow: none !important; filter: none !important; transition: none 0s ease 0s !important; overflow: visible !important; outline: none !important; visibility: visible !important; cursor: pointer !important; height: 16px !important; width: 16px !important; }html > x-root-ktbk4#pb_rl61mm5jrh5 > x-icon-o3bfq[a59iuf] { background: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/Pgo8c3ZnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgaGVpZ2h0PSIxNiIgd2luZHRoPSIxMDI0IiB3aWR0aD0iMTYiPgogIDxwYXRoIGQ9Ik03NjcuMDgzIDc1OC4xNDRDODk5LjA5NCA1MzIuMjg4IDk2OS44NTYgMjczLjk2MyA5NjkuODU2IDcuNjM3aC02MC44ODVWOTMuMjlDODAyLjI0IDM0LjA2OSA2ODIuNTM5IDIuOTIyIDU2MC4wNjQgMi45MjJjLTExNy4wOTkgMC0yMzEuNzg3IDI5LjA1Ni0zMzQuNTQ5IDg0LjMzMVY3LjYzN2gtNjAuNjA4YzAgMjY2LjMyNSA3MC43NjMgNTI0LjY1MSAyMDIuNzczIDc1MC41MDdoLTYzLjM4MWMtMTMuNTY4LTY4LjEzOS03My40NzItMTE5LjYxNi0xNDUuMTUyLTExOS42MTYtODEuNjY0IDAtMTQ4LjA3NSA2Ni44MTYtMTQ4LjA3NSAxNDguOTA3czY2LjQzMiAxNDguOTA3IDE0OC4wNzUgMTQ4LjkwN2M3MS42OCAwIDEzMS41ODQtNTEuNDk5IDE0NS4xNTItMTE5LjYxNmg5OS41MmExNDg4Ljk0IDE0ODguOTQgMCAwIDAgMTQxLjk1MiAxODUuMjE2bDIxLjYxMSAyNCAyMS42MTEtMjRhMTQ4NS4zNDcgMTQ4NS4zNDcgMCAwIDAgMTQxLjk3My0xODUuMjE2aDEwNi4xNzZ2MTAyLjI3Mmg1OC4yNFY4MTYuNzI2aDYzLjIzMnYxMDIuMjcyaDU4LjI4M1Y3NTguMTQ1SDc2Ny4wODR6TTE1OS4xNDcgODc3LjczOWMtNDkuNTE1IDAtODkuNzkyLTQwLjUxMi04OS43OTItOTAuMjgzIDAtNDkuNzkyIDQwLjI3Ny05MC4yNjEgODkuNzkyLTkwLjI2MSA0OS40OTMgMCA4OS43NzEgNDAuNDY5IDg5Ljc3MSA5MC4yNjEuMDIxIDQ5Ljc0OS00MC4yNTYgOTAuMjgzLTg5Ljc3MSA5MC4yODN6bTEyMS41NzgtNTIwLjA2NGMwLTcxLjM4MSA1Ny43NzEtMTI5LjQ3MiAxMjguNzQ3LTEyOS40NzIgNzEuMDE5IDAgMTI4Ljc0NyA1OC4wOTEgMTI4Ljc0NyAxMjkuNDcydjczLjM0NGg1OC4zMDR2LTczLjM0NGMwLTcxLjM4MSA1Ny43MjgtMTI5LjQ3MiAxMjguNzQ3LTEyOS40NzIgNzAuOTk3IDAgMTI4Ljc0NyA1OC4wOTEgMTI4Ljc0NyAxMjkuNDcyIDAgMTYwLjkxNy0xMjguNTk3IDI5MS44NC0yODYuNjc3IDI5MS44NC0xNTguMDE2IDAtMjg2LjYxMy0xMzAuOTAxLTI4Ni42MTMtMjkxLjg0em0yNzkuMzE4LTI5Ni4xNWMxMjEuNDcyIDAgMjM5Ljg3MiAzMy4zMjMgMzQzLjU1MiA5Ni4zODQtMy43NTUgMzYuMTYtOC45MzkgNzIuMDY0LTE1LjQyNCAxMDcuNjI3LTMyLjEyOC01Ny4xOTUtOTMuMDU2LTk1Ljk1Ny0xNjIuOTAxLTk1Ljk1Ny02Ni40MzIgMC0xMjQuNzM2IDM1LjA5My0xNTcuOTA5IDg3LjcwMS0zMy4xNzMtNTIuNjA4LTkxLjQ3Ny04Ny43MDEtMTU3Ljg4OC04Ny43MDEtNjkuODAzIDAtMTMwLjcwOSAzOC43NDEtMTYyLjg1OSA5NS44OTMtNi44NDgtMzcuNjExLTEyLjI2Ny03NS41NjMtMTYuMDg1LTExMy43OTIgOTkuOTA0LTU5LjAwOCAyMTMuNDE5LTkwLjE1NSAzMjkuNTE1LTkwLjE1NXpNMzc0LjM3OSA2NDhjNTUuMTA0IDM3Ljk1MiAxMjEuNTU3IDYwLjEzOSAxOTMuMDAzIDYwLjEzOSA3MS40ODggMCAxMzcuOTYzLTIyLjE4NyAxOTMuMDY3LTYwLjE2LTE4Ljc5NSAzNy41NjgtMzkuMzM5IDc0LjI4My02MS40ODMgMTEwLjE2NUg0MzUuNzk4QTE0MTguOTMyIDE0MTguOTMyIDAgMCAxIDM3NC4zNzkgNjQ4em0xOTMuMDAyIDI5MC4wMjdjLTMzLjM4Ny0zOC44NjktNjQuNDkxLTc5LjQwMy05My4zMTItMTIxLjMwMWgxODYuNjY3Yy0yOC44MjEgNDEuODk5LTU5LjkyNSA4Mi40MTEtOTMuMzU1IDEyMS4zMDF6TTQwOS40NzIgMzAzLjI1M2MtMjkuODg4IDAtNTQuMTIzIDI0LjM4NC01NC4xMjMgNTQuNDIxIDAgNy4xODkgMS40NzIgMTQuMDM3IDMuOTg5IDIwLjMwOSA0MS42MjEtMjQuNDQ4IDc4LjU0OS0yLjk0NCA5NS4wNjEgMTAuMDQ4YTU0LjQzMyA1NC40MzMgMCAwIDAgOS4xOTUtMzAuMzU3YzAtMzAuMDM3LTI0LjIxMy01NC40MjEtNTQuMTIzLTU0LjQyMXptMzY2LjQgNzMuMzIzYzIuMTc2LTUuOTA5IDMuNTQxLTEyLjIwMyAzLjU0MS0xOC45MDEgMC0zMC4wMzctMjQuMjM1LTU0LjQyMS01NC4xMDEtNTQuNDIxLTI5LjkzMSAwLTU0LjE2NSAyNC4zODQtNTQuMTY1IDU0LjQyMSAwIDExLjkwNCAzLjkwNCAyMi44MDUgMTAuMzQ3IDMxLjc2NSAxNS4yMzItMTIuNDggNTIuMjQ1LTM1Ljg4MyA5NC4zNzktMTIuODY0eiIgc3R5bGU9ImZpbGw6ICMwMGFlOTI7Ii8+Cjwvc3ZnPg==") center center / 16px 16px no-repeat !important; border: 0px !important; border-radius: 0px !important; left: -16px !important; top: -16px !important; right: initial !important; bottom: initial !important; margin: 0px !important; padding: 0px !important; position: absolute !important; transform: none !important; z-index: 2147483647 !important; box-shadow: none !important; filter: none !important; transition: none 0s ease 0s !important; overflow: visible !important; outline: none !important; visibility: visible !important; cursor: pointer !important; height: 16px !important; width: 16px !important; }html > x-root-ktbk4#pb_rl61mm5jrh5 > canvas[x-icon-o3bfq] { background: none center center / 16px 16px no-repeat !important; border: 0px !important; border-radius: 0px !important; left: -16px !important; top: -16px !important; right: initial !important; bottom: initial !important; margin: 0px !important; padding: 0px !important; position: absolute !important; transform: none !important; z-index: 2147483647 !important; box-shadow: none !important; filter: none !important; transition: none 0s ease 0s !important; overflow: visible !important; outline: none !important; visibility: visible !important; cursor: pointer !important; height: 16px !important; width: 16px !important; } arPreserve **/</style><style media=""></style><link rel="stylesheet" type="text/css" href="/-/build/static/css/7139.5242abde.chunk.css"><title>Codex Leicester Chat App · Streamlit</title><script src="https://cdn.heapanalytics.com/js/replay/9075-Streamlit-prod-heap/container.js" data-cfasync="false" async="true" data-vendor="auryc" data-role="container" charset="utf-8"></script><style data-id="immersive-translate-input-injected-css">.immersive-translate-input {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  z-index: 2147483647;
  display: flex;
  justify-content: center;
  align-items: center;
}

.immersive-translate-loading-spinner {
  vertical-align: middle !important;
  width: 10px !important;
  height: 10px !important;
  display: inline-block !important;
  margin: 0 4px !important;
  border: 2px rgba(221, 244, 255, 0.6) solid !important;
  border-top: 2px rgba(0, 0, 0, 0.375) solid !important;
  border-left: 2px rgba(0, 0, 0, 0.375) solid !important;
  border-radius: 50% !important;
  padding: 0 !important;
  -webkit-animation: immersive-translate-loading-animation 0.6s infinite linear !important;
  animation: immersive-translate-loading-animation 0.6s infinite linear !important;
}

@-webkit-keyframes immersive-translate-loading-animation {
  from {
    -webkit-transform: rotate(0deg);
  }

  to {
    -webkit-transform: rotate(359deg);
  }
}

@keyframes immersive-translate-loading-animation {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(359deg);
  }
}


.immersive-translate-input-loading {
  --loading-color: #f78fb6;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  display: block;
  margin: 12px auto;
  position: relative;
  color: white;
  left: -100px;
  box-sizing: border-box;
  animation: immersiveTranslateShadowRolling 1.5s linear infinite;
}

@keyframes immersiveTranslateShadowRolling {
  0% {
    box-shadow: 0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);
  }

  12% {
    box-shadow: 100px 0 var(--loading-color), 0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);
  }

  25% {
    box-shadow: 110px 0 var(--loading-color), 100px 0 var(--loading-color), 0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);
  }

  36% {
    box-shadow: 120px 0 var(--loading-color), 110px 0 var(--loading-color), 100px 0 var(--loading-color), 0px 0 rgba(255, 255, 255, 0);
  }

  50% {
    box-shadow: 130px 0 var(--loading-color), 120px 0 var(--loading-color), 110px 0 var(--loading-color), 100px 0 var(--loading-color);
  }

  62% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 130px 0 var(--loading-color), 120px 0 var(--loading-color), 110px 0 var(--loading-color);
  }

  75% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0), 130px 0 var(--loading-color), 120px 0 var(--loading-color);
  }

  87% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0), 130px 0 var(--loading-color);
  }

  100% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0);
  }
}


.immersive-translate-search-recomend {
  border: 1px solid #dadce0;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  position: relative;
  font-size: 16px;
}

.immersive-translate-search-enhancement-en-title {
  color: #4d5156;
}

/* dark */
@media (prefers-color-scheme: dark) {
  .immersive-translate-search-recomend {
    border: 1px solid #3c4043;
  }

  .immersive-translate-close-action svg {
    fill: #bdc1c6;
  }

  .immersive-translate-search-enhancement-en-title {
    color: #bdc1c6;
  }
}


.immersive-translate-search-settings {
  position: absolute;
  top: 16px;
  right: 16px;
  cursor: pointer;
}

.immersive-translate-search-recomend::before {
  /* content: " "; */
  /* width: 20px; */
  /* height: 20px; */
  /* top: 16px; */
  /* position: absolute; */
  /* background: center / contain url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAxlBMVEUAAADpTInqTIjpSofnSIfqS4nfS4XqS4nqTIjsTYnrTInqTIroS4jvQIDqTIn////+/v7rSYjpTIn8/v7uaZzrTIr9/f3wfansWJL88/b85e73qc39+/v3xNnylrvrVI/98fb62Obva5/8+fr76vH4y9zpSIj74e353Oj1ocTzm77xhK/veKbtYpjsXJTqU47oTInxjrXyh7L99fj40eH2ttH1udD3sc31ssz1rMnykLXucqPtbqD85e/1xdn2u9DzqcXrUY6FaJb8AAAADnRSTlMA34BgIM8Q37/fz7+/EGOHcVQAAAGhSURBVDjLhZPncuowEEZFTW7bXVU7xsYYTO/p7bb3f6lICIOYJOT4h7/VnFmvrBFjrF3/CR/SajBHswafctG0Qg3O8O0Xa8BZ6uw7eLjqr30SofCDVSkemMinfL1ecy20r5ygR5zz3ArcAqJExPTPKhDENEmS30Q9+yo4lEQkqVTiIEAHCT10xWERRdH0Bq0aCOPZNDV3s0xaYce1lHEoDHU8wEh3qRJypNcTAeKUIjgKMeGLDoRCLVLTVf+Ownj8Kk6H9HM6QXPgYjQSB0F00EJEu10ILQrs/QeP77BSSr0MzLOyuJJQbnUoOOIUI/A8EeJk9E4YUHUWiRyTVKGgQUB8/3e/NpdGlfI+FMQyWsCBWyz4A/ZyHXyiiz0Ne5aGZssoxRmcChw8/EFKQ5JwwkUo3FRT5yXS7q+Y/rHDZmFktzpGMvO+5QofA4FPpEmGw+EWRCFvnaof7Zhe8NuYSLR0xErKLThUSs8gnODh87ssy6438yzbLzxl012HS19vfCf3CNhnbWOL1eEsDda+gDPUvri8tSZzNFrwIZf1NmNvqC1I/t8j7nYAAAAASUVORK5CYII='); */
}

.immersive-translate-search-title {}

.immersive-translate-search-title-wrapper {}

.immersive-translate-search-time {
  font-size: 12px;
  margin: 4px 0 24px;
  color: #70757a;
}

.immersive-translate-expand-items {
  display: none;
}

.immersive-translate-search-more {
  margin-top: 16px;
  font-size: 14px;
}

.immersive-translate-modal {
  display: none;
  position: fixed;
  z-index: 2147483647;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.4);
  font-size: 15px;
}

.immersive-translate-modal-content {
  background-color: #fefefe;
  margin: 10% auto;
  padding: 40px 24px 24px;
  border: 1px solid #888;
  border-radius: 10px;
  width: 80%;
  max-width: 270px;
  font-family: system-ui, -apple-system, "Segoe UI", "Roboto", "Ubuntu",
    "Cantarell", "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol", "Noto Color Emoji";
  position: relative
}

.immersive-translate-modal .immersive-translate-modal-content-in-input {
  max-width: 500px;
}
.immersive-translate-modal-content-in-input .immersive-translate-modal-body {
  text-align: left;
  max-height: unset;
}

.immersive-translate-modal-title {
  text-align: center;
  font-size: 16px;
  font-weight: 700;
  color: #333333;
}

.immersive-translate-modal-body {
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  color: #333333;
  word-break: break-all;
  margin-top: 24px;
}

@media screen and (max-width: 768px) {
  .immersive-translate-modal-body {
    max-height: 250px;
    overflow-y: auto;
  }
}

.immersive-translate-close {
  color: #666666;
  position: absolute;
  right: 16px;
  top: 16px;
  font-size: 20px;
  font-weight: bold;
}

.immersive-translate-close:hover,
.immersive-translate-close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.immersive-translate-modal-footer {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 24px;
}

.immersive-translate-btn {
  width: fit-content;
  color: #fff;
  background-color: #ea4c89;
  border: none;
  font-size: 16px;
  margin: 0 8px;
  padding: 9px 30px;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.immersive-translate-btn:hover {
  background-color: #f082ac;
}

.immersive-translate-cancel-btn {
  /* gray color */
  background-color: rgb(89, 107, 120);
}


.immersive-translate-cancel-btn:hover {
  background-color: hsl(205, 20%, 32%);
}

.immersive-translate-action-btn {
  background-color: transparent;
  color: #EA4C89;
  border: 1px solid #EA4C89
}

.immersive-translate-btn svg {
  margin-right: 5px;
}

.immersive-translate-link {
  cursor: pointer;
  user-select: none;
  -webkit-user-drag: none;
  text-decoration: none;
  color: #007bff;
  -webkit-tap-highlight-color: rgba(0, 0, 0, .1);
}

.immersive-translate-primary-link {
  cursor: pointer;
  user-select: none;
  -webkit-user-drag: none;
  text-decoration: none;
  color: #ea4c89;
  -webkit-tap-highlight-color: rgba(0, 0, 0, .1);
}

.immersive-translate-modal input[type="radio"] {
  margin: 0 6px;
  cursor: pointer;
}

.immersive-translate-modal label {
  cursor: pointer;
}

.immersive-translate-close-action {
  position: absolute;
  top: 2px;
  right: 0px;
  cursor: pointer;
}</style><link id="favicon" rel="icon" href="//codexleicester.streamlit.app/~/+//favicon.png"><link id="alternate-favicon" rel="alternate icon" href="//codexleicester.streamlit.app/~/+//favicon.png"></head>


<x-root-ktbk4 id="pb_rl61mm5jrh5" style="background: none !important; border: 0px !important; border-radius: 0px !important; left: -16px !important; top: -16px !important; right: initial !important; bottom: initial !important; width: 16px !important; height: 16px !important; margin: 0px !important; padding: 0px !important; position: absolute !important; transform: none !important; z-index: 2147483647 !important; box-shadow: none !important; filter: none !important; transition: none 0s ease 0s !important; overflow: visible !important; outline: none !important; visibility: hidden !important;"><style></style></x-root-ktbk4>


<body><noscript>You need to enable JavaScript to run this app.</noscript><div id="root"><div class="" style=""><div class="styles_streamlitAppContainer__w82h8"><div class="styles_stateContainer__CelYF"><a href="https://streamlit.io/cloud?__hstc=225580997.d5ea96a02ce85e3a075128031957027f.1705379952354.1708070958877.1708074247137.18&amp;__hssc=225580997.1.1708074247137&amp;__hsfp=3535770217" target="_blank" rel="noopener noreferrer" class="viewerBadge_container__r5tak styles_viewerBadge__CvC9N"><div class="viewerBadge_link__qRIco"><svg width="303" height="165" viewBox="0 0 303 165" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M151.478 102.737L98.4421 74.7024L6.37999 26.0452C6.29595 25.9612 6.12789 25.9612 6.04385 25.9612C2.68239 24.3645 -0.763116 27.7259 0.497434 31.0874L47.4067 150.73L47.4151 150.756C47.4655 150.873 47.5075 150.991 47.558 151.109C49.4824 155.571 53.6842 158.327 58.2558 159.411C58.6424 159.495 58.919 159.572 59.3831 159.664C59.845 159.767 60.4912 159.907 61.0458 159.949C61.1383 159.958 61.2223 159.958 61.3148 159.966H61.382C61.4492 159.974 61.5164 159.974 61.5837 159.983H61.6761C61.7349 159.991 61.8022 159.991 61.861 159.991H61.9702C62.0375 160 62.1047 160 62.1719 160V160C121.295 166.446 181.803 166.446 240.926 160V160C241.641 160 242.338 159.966 243.01 159.899C243.229 159.874 243.439 159.848 243.649 159.823C243.674 159.815 243.708 159.815 243.733 159.806C243.876 159.79 244.019 159.764 244.162 159.739C244.372 159.714 244.582 159.672 244.792 159.63C245.212 159.537 245.403 159.47 245.973 159.274C246.543 159.078 247.49 158.736 248.083 158.45C248.675 158.164 249.086 157.89 249.582 157.579C250.196 157.193 250.779 156.797 251.371 156.354C251.626 156.158 251.801 156.033 251.986 155.857L251.885 155.798L151.478 102.737Z" fill="#FAFAFA"></path><path d="M296.729 26.0464H296.645L204.549 74.7036L255.744 150.95L302.536 31.0886V30.9205C303.712 27.391 300.098 24.1976 296.729 26.0464" fill="#A3A8B8"></path><path d="M156.386 2.91088C154.033 -0.526222 148.906 -0.526222 146.638 2.91088L98.4424 74.7035L151.478 102.738L251.986 155.857C252.617 155.239 253.123 154.637 253.658 154.001C254.415 153.068 255.121 152.068 255.742 150.95L204.547 74.7035L156.386 2.91088Z" fill="#D5DAE5"></path></svg></div></a><iframe allow="accelerometer; ambient-light-sensor; autoplay; battery; camera; clipboard-write; document-domain; encrypted-media; fullscreen; geolocation; gyroscope; layout-animations; legacy-image-formats; magnetometer; microphone; midi; oversized-images; payment; picture-in-picture; publickey-credentials-get; sync-xhr; usb; vr ; wake-lock; xr-spatial-tracking" sandbox="allow-forms allow-modals allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-downloads" height="auto" title="streamlitApp" src="//codexleicester.streamlit.app/~/+/" class="styles_iframe__y4AbF"></iframe></div></div></div><div class="" style=""></div></div><audio class="audio-output" style="display: none;"></audio><div id="volume-booster-visusalizer">
    <div class="sound">
        <div class="sound-icon"></div>
        <div class="sound-wave sound-wave_one"></div>
        <div class="sound-wave sound-wave_two"></div>
        <div class="sound-wave sound-wave_three"></div>
    </div>
    <div class="segments-box">
        <div data-range="1-20" class="segment"><span></span></div>
        <div data-range="21-40" class="segment"><span></span></div>
        <div data-range="41-60" class="segment"><span></span></div>
        <div data-range="61-80" class="segment"><span></span></div>
        <div data-range="81-100" class="segment"><span></span></div>
    </div>
</div></body>


</html>
















# load the Environment Variables. 
load_dotenv()
st.set_page_config(page_title="Codex Leicester Chat App")

# Sidebar contents
with st.sidebar:
    st.title('Your personal AI')
    st.markdown('''

    
   ## Be educated, be organised, and be agitated
- [LAION-AI](https://laion.ai/)
    The LLM for Codex Leicester is trained using LAION-AI.
    
    ''')

   


    
    add_vertical_space(3)
    st.markdown('<p style="font-family:monospace; color: Red;">Made by Chanchal C. Ganvir</p>', unsafe_allow_html=True)


st.markdown('<p style="font-family:larg-cursive;font-size:40px; color:Green;text-shadow: 14 14 20px black;">Codex Leicester</p>', unsafe_allow_html=True)


def main():

    # Generate empty lists for generated and user.
    ## Assistant Response
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hey there, great to meet you. I’m Codex Leicester, your personal AI. My goal is to be useful, friendly and providing information. Ask me for advice, for answers, or let’s talk about whatever’s on your mind. "]

    ## user question
    if 'user' not in st.session_state:
        st.session_state['user'] = ['Hi!']

    # Layout of input/response containers
    response_container = st.container()
    colored_header(label='', description='', color_name='blue-70')
    input_container = st.container()

    # get user input
    def get_text():
        input_text = st.text_input("You: ", "", key="input")
        return input_text

    ## Applying the user input box
    with input_container:
        user_input = get_text()

    def chain_setup():


        template = """<|prompter|>{question}<|endoftext|>
        <|assistant|>"""

     
        
        prompt = PromptTemplate(template=template, input_variables=["question"])

        llm=HuggingFaceHub(repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", model_kwargs={"max_new_tokens":1200})

        llm_chain=LLMChain(
            llm=llm,
            prompt=prompt
        )
        return llm_chain


    # generate response
    def generate_response(question, llm_chain):
        response = llm_chain.run(question)
        return response

    ## load LLM
    llm_chain = chain_setup()

    # main loop
    with response_container:
        if user_input:
            response = generate_response(user_input, llm_chain)
            st.session_state.user.append(user_input)
            st.session_state.generated.append(response)
            
        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state['user'][i], is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))

if __name__ == '__main__':
    main()
