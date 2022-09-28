// ==UserScript==
// @name         scratch
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Dong
// @match        https://scratch.mit.edu/*/*
// @icon         https://scratch.mit.edu/favicon.ico
// @grant        none
// ==/UserScript==

(function() {
    function addScript(url){
        document.write("<script language=javascript src="+url+"></script>");
    }
    addScript('https://www.gstatic.com/firebasejs/4.12.1/firebase.js')
    addScript('https://www.gstatic.com/firebasejs/4.12.1/firebase-firestore.js')
    var namespan=document.getElementsByClassName('account-nav_profile-name_2oRiV')
    console.log(namespan.innerText)
})();