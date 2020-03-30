===========
To Do List
===========

- 改善点のリストアップ


-------

- imageの使い分け
-----------------

- 複数Dockerimageを作っておいて、docker-composeの.envでどれを使うか決めるイメージ
    - 構成を今よりシンプルにする
    - docker-compose側から使うイメージを制御出来るとより望ましい
        - 仕様上難しいかもしれない
            - (Dockerにおけるsymbolic linkの扱いなど)
            - 最終的に使用するベースのイメージは1つに決定させるべきなので、それまでのつなぎと位置づけるべきな気がする

- DBとの連携
    - RDBを立ち上げて、docker-composeで紐づけて連携させておく
        - GIS機能つきのPostgreSQLを使えると望ましい
    - SQLAlchaemyの使い方も確認しておく必要


- proxyの調査
    - upstreamとか
    - 優先度は低い

