console.log(new Date())

console.log(Date())

console.log(Date.now()) //unix epoc time, tid siden 1970 i seconder

//ISO 8601, iso standard for date, YYYY-MM-DD, python and java fallows this standard but old c++ dosen't

//intl, formats time

const date = new Date();

const danishDate = new Intl.DateTimeFormat("da-dk").format(date);
console.log(danishDate);

const amercanDate = Intl.DateTimeFormat("en-us").format(date);
console.log(amercanDate)

