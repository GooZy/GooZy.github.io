./node_modules/.bin/hexo clean
./node_modules/.bin/hexo generate
./node_modules/.bin/hexo deploy
./node_modules/.bin/hexo clean
git add -A
git commit -m 'update'
git push
