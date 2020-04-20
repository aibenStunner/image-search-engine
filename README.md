<h1 align="left">
    Image Search Engine
</h1>
  <p align="center">
 <img src="https://img.shields.io/github/release/aibenStunner/image-search-engine.svg" />
 <img src="https://img.shields.io/github/issues/aibenStunner/image-search-engine.svg">
 <img src="https://img.shields.io/github/issues-closed-raw/aibenStunner/image-search-engine.svg">
 <img src="https://requires.io/github/aibenStunner/image-search-engine/requirements.svg?branch=master"> 
 <img src="https://img.shields.io/snyk/vulnerabilities/github/aibenStunner/image-search-engine.svg">
 <img src="https://img.shields.io/github/languages/top/aibenStunner/image-search-engine.svg">
 <img src="https://img.shields.io/codefactor/grade/github/aibenStunner/image-search-engine/master.svg">

 </p>

A simple image search engine built from the concept of Content-Based Image Retrieval (CBIR) systems.:sweat_smile:

## Features :gem:
   * Written in uncomplicated python :innocent:
   * Displays fairly all images related to the search query :droplet:
   * Works on Mac, Linux and Windows

## Installation :package:
1. Clone the repo
```bash
   $ git clone https://github.com/aibenStunner/image-search-engine.git
   $ cd image-search-engine
```
2. Install dependencies
```bash
   $ pip install -r requirements.txt
```

## Usage :computer:
* You'll need a dataset of images to work on. A sample dataset can be gotten from here <a href="http://lear.inrialpes.fr/people/jegou/data.php">INRIA Holidays Dataset.</a>

* To index the sample dataset, open up a shell and issue the following command:
```bash
    $ python index.py --dataset dataset --index index.csv
```

* To perform search on the dataset, issue the command:
```bash
    $ python search.py --index index.csv --query <path-to-image-search-query> --result-path dataset
```

## Demo :movie_camera:
   Search results from query:
   
   ![](res/query.png)
   ![](res/results.png)
   
 
 ## Contributing :gift: [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## Want to talk more??
 If you are interested in helping or have something to suggest or just want to chat with me, you can reach me through the following media .
* Email - ebenezergadri99@gmail.com :e-mail:
* Let's connect on <a href="https://www.linkedin.com/in/ebenezer-kweku-gadri-akrong-22b19a185/">LinkedIn.</a> :pushpin:
* I'm on <a href="https://www.hackerrank.com/aiben_">HackerRank</a> too.:relaxed:

## References :book:
<a href="https://en.wikipedia.org/wiki/Content-based_image_retrieval">Content-Based Image Retrieval (CBIR)</a>

## Todos :pencil:
 - Improve on quality of search
 - Integrate it into applications
 - Write tests

License :key:
----

MIT &copy; Gadri Ebenezer

