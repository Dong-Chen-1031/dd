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
    setTimeout(() => {
        
        var namespan=document.getElementsByClassName('profile-name')
        console.log(namespan[0].innerText)
    }, 5000);
})();