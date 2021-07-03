/*
In order for the image stream to be constant a refresh to the api must be called.
*/
// initialize camera for wifi connection 
// http://192.168.1.183/cam.cgi?cam.cgi?mode=getinfo&type=capability
const puppeteer = require('puppeteer');
var myArgs = process.argv.slice(2);

async function performRefresh(){
return new Promise(async function(resolve, reject) {
  const browser = await puppeteer.launch()
  const page = await browser.newPage()
  await page.setDefaultNavigationTimeout(0)

    var response = await page.goto('http://'+myArgs+'/cam.cgi?mode=startstream&value=9100')
    page.on('console', msg => console.log(msg.text()));
    var pageXML = await response.text()
    await browser.close()

   if(pageXML.toString().indexOf("err")!=-1){
    console.log('we have a problem..')
    console.log(pageXML)
    return resolve(false);
    }
    return resolve(true);
    });
}

async function napTime(milliseconds) {
return new Promise(async function(resolve, reject) {
  if(milliseconds == null){
    milliseconds = 2000;
  }
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
  return resolve(true)
});
}



(async () => {
let cameraStatus = true;
do{
let cameraStatus = await performRefresh();
await napTime(10000)
}while(cameraStatus)
console.log("we had some issues...")
process.exit();
})()
