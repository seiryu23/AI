以下をコマンドラインで実行し、素材情報をコンバート

cd {Profile}\Desktop\Python開発\AI
{Profile}\AppData\Roaming\Python\Python39\Scripts\pyrcc5 -o qt_resource_rc.py qt_resource.qrc
※{Profile}はUserディレクトリパス

【必須】環境変数に以下を追加し、再起動する
name：QT_QPA_PLATFORM_PLUGIN_PATH
value：{Profile}\AppData\Roaming\Python\Python39\site-packages\PyQt5\Qt\plugins\platforms
