```bash
brew install ruby
```

in zshrc

```bash
if [ -d "/opt/homebrew/opt/ruby/bin" ]; then
  export PATH=/opt/homebrew/opt/ruby/bin:$PATH
  export PATH=`gem environment gemdir`/bin:$PATH
fi
```

in sizhky.github.io

```bash
gem install bundler
bundle update
```
finally
```bash
jekyll serve --watch --port 4001
```