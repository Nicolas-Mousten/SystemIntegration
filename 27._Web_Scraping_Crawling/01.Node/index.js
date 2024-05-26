import fs from "fs";

// var response = await fetch("https://www.proshop.dk/Baerbar-computer");
// const result = await response.text();

// fs.writeFileSync("index.html", result);
import {load} from "cheerio";

const htmlPageString = fs.readFileSync("index.html").toString();

const $ = load(htmlPageString);

$("#products [product]").each((index, element) => {
    const name = $(element).find(".site-product-link h2").text();
    const description = $(element).find(".site-product-link").text();
    const price = $(element).find(".site-currency-lg").text();
    
    console.log(name)
    //console.log(description)
    console.log(price)
    console.log("==============")
});