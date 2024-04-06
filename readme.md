# 概要
https://www.youtube.com/watch?v=EQIAzH0HvzQ

の模写
# 動作環境
- windows 11
- python 3.12
# 環境変数
- microsoft版のpythonなので、pipでインストールしたパッケージのpathが通ってなかった
- https://zenn.dev/kumazo/articles/35215498b86939 を参考にpathを通した
# 起動
ターミナルのディレクトリが.../flask_sapleの状態で
```shell
$env:FLASK_APP = "flaskr"

$env:FLASK_ENV = "development"

$env:FLASK_DEBUG = 1  

flask run
```
で起動

最近のflaskでは`$env:FLASK_ENV = "development"`はいらないらしい