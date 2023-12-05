const puppeteer = require('puppeteer');
const cheerio = require('cheerio');
// const utils = require("./utils");

async function handleScraping() {
    let browser = null
    let sendData = [];
    async function init() {
        browser = await puppeteer.launch({
            headless: false, // Use the new Headless mode
            // ... other options
        });
    }

    // for Cricket page
    async function launchBrowser() {
        const page = await browser.newPage();
        
        // await page.setRequestInterception(true);

        // // Listen for the 'response' event
        // page.on('response', async (response) => {

        //     let count = 0;
            
        //     const url = response.url();
        //     // console.log("ajax url >>> ", url);

        //     // Check if the response URL matches the desired URL
        //     if (url === 'https://www.mercadopublico.cl/BuscarLicitacion/Home/Buscar') {
        //         const responseBody = await response.text();
        //         // console.log("response >>> ", responseBody);
        //         const $ = cheerio.load(responseBody);
                
        //         const idList = [];
        //         $('span.clearfix').each((i, element) => {
        //             if (i%2 == 1) {
        //                 const id = $(element).text();
        //                 idList.push(id);
        //             }
        //         });

        //         const titleList = [];
        //         $('h2.text-weight-light').each((i, element) => {
        //             const title = $(element).text();
        //             titleList.push(title);
        //         });

        //         const descList = [];
        //         $('p.text-weight-light').each((i, element) => {
        //             const desc = $(element).text();
        //             descList.push(desc);
        //         });

        //         const budgetList = [];
        //         $('div.monto-dis').each((i, element) => {
        //             const budget = $(element).text();
        //             try {
        //                 budget.replace("Monto disponible", "");
        //             } catch (error) {}
        //             try {
        //                 budget.replace("Monto estimado", "");
        //             } catch (error) {}
        //             try {
        //                 budget.replace("Monto", "");
        //             } catch (error) {}
        //             budgetList.push(budget);
        //         });
                
        //         // const postDateList = [];
        //         // $('//*[@id="searchResults"]/div[1]/div/div/div[2]/div[3]/div[2]/span').each((i, element) => {
        //         //     const postDate = $(element).text();
        //         //     postDateList.push(postDate);
        //         // });

        //         // // xpath.select('//*[@id="searchResults"]/div[1]/div/div/div[2]/div[3]/div[2]/span', $).each((i, element) => {
        //         // //     const postDate = $(element).text();
        //         // //     postDateList.push(postDate);
        //         // // });
                
        //         // const deadlineList = [];
        //         // $('//*[@id="searchResults"]/div[1]/div/div/div[2]/div[3]/div[3]/span[1]').each((i, element) => {
        //         //     const deadline = $(element).text();
        //         //     deadlineList.push(deadline);
        //         // });
                
        //         for (let j = 0; j < titleList.length; j++) {
        //             const id = idList[j].trim();
        //             console.log("id >>>", id)
        //             const title = titleList[j].trim();
        //             console.log("title >>>", title)
        //             const desc = descList[j].trim();
        //             console.log("desc >>> ", desc);
        //             const budget = budgetList[j].trim();
        //             console.log("budget >>> ", budget);
        //             // const postDate = postDateList[j].trim();
        //             // console.log("postDate >>> ", postDate);
        //             // const deadline = deadlineList[j].trim();
        //             // console.log("deadline >>> ", deadline);
        //             const postDate = "postDate";
        //             console.log("postDate >>> ", postDate);
        //             const deadline = "deadline";
        //             console.log("deadline >>> ", deadline)
        //             const resultData = {id, title, desc, budget, postDate, deadline};
        //             // sendData.push(resultData);
                                        
        //             // const parser = new Parser();
        //             const csv = parser.parse(resultData);
                
        //             const csvDataWithoutHeader = csv.split('\n')[1] + '\n';
                    
        //             fs.appendFileSync('ScrapedJobs.csv', csvDataWithoutHeader, 'utf8', (err) => {
        //                 if (err) {
        //                     console.error('Error appending to CSV file:', err);
        //                 } else {
        //                     console.log('CSV data appended successfully.');
        //                 }
        //             });
                    
        //             console.log("send data count >>> ", sendData.length);
        //             const toServerData = {data: sendData};
        //             await sendToServer(resultData);
        //             console.log("----------------------------------------------------");
        //         }
        //     }
        // });
        
        // // Disable request interception
        // // await page.setRequestInterception(false);
        
        // Navigate to a page that triggers AJAX requests
        await page.goto('https://helloalma.com/', {
            waitUntil: 'load',
            timeout: 0,
          });
        console.log("page loaded!");
        
        // // Wait for the page to load.
        
        // Delay function
        function delay(ms) {
            return new Promise((resolve) => setTimeout(resolve, ms));
        }
            
        // // await page.waitForNavigation();
        // await page.evaluate(() => {
        //     window.scrollTo(0, document.documentElement.scrollHeight);
        // });
        
        // delay
        await delay(3000);

        var iframeElement = await page.$('#form-iframe');

        for(var index=2; index<688; index++)
        {
            var frame = await iframeElement.contentFrame();
            var flag = false;

            flag =  await frame.evaluate((index) => {
                
                $.Busqueda.buscar(index);
                // const nextBtn = $('.next-pager')

                // if (nextBtn != null) {
                //     nextBtn.trigger('click');
                //     return false;
                // } else {
                //     return true;
                // }        
            }, index);
            await delay(200);

            if(flag)
                break;
        }

        await page.waitForNavigation();

        // await browser.close();
    }
    
    async function sendToServer(data) {
        // console.log(data);
        fetch(`http://localhost:8000/scrapedData`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then((response) => {
        console.log("success");
        // Handle the response data
        })
        .catch((error) => {
        console.error("error",error);
        // Handle any errors that occurred during the request
        });
    }

    // lunch main code for Cricket
    await init();
    await launchBrowser();
    
}

// setInterval(() => {
    // lunch full code
    handleScraping().then(res => {
        // console.log('handle scraping have done!!')
    })
// }, 36000000);
