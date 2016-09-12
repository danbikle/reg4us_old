# README

This repo was built to help students during class03 of my Machine Learning Applications class:

http://www.ml4.us/cclasses/class03#psy

This repo compares effectiveness of GSPC predictions computed from Linear Regression and Logistic Regression.

This repo is a mash-up-app of Rails and Python.

Here I use Rails to serve static content.

I use Python to generate some of the static content each night after the market has closed and the most recent GSPC-closing-price is available from Yahoo.

I use the shell-commands below to deploy this repo to my laptop and then start the web-server:

```bash
cd ~
git clone https://github.com/danbikle/reg4us
cd reg4us
bundle install
bin/rails s
```

The above shell commands work well if you run them in this VirtualBox instance:

https://s3-us-west-2.amazonaws.com/ml4us/ub16aug13d.ova

The password of the ann account in the above instance is 'a'.

If you want to see a running copy of this repo, it should be listening for you at this URL:

http://www.reg4.us

If you have questions, e-me: bikle101@gmail.com

