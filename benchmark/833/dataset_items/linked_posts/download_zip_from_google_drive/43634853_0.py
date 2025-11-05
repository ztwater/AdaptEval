// ==UserScript==
// @name         Bypass Google drive virus scan
// @namespace    SmartManoj
// @version      0.1
// @description  Quickly get the download link
// @author       SmartManoj
// @match        https://drive.google.com/uc?id=*&export=download*
// @grant        none
// ==/UserScript==

    function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }

    async function demo() {
        await sleep(5000);
        window.close();
    }

    (function() {
        location.replace(document.getElementById("uc-download-link").href);
        demo();
    })();
