import os
from PIL import Image

def gif_to_sprite_sheet(gif_path, output_path):
    # GIF画像を開く
    gif = Image.open(gif_path)
    
    # フレーム数を取得
    frames = []
    try:
        while True:
            frames.append(gif.copy())
            gif.seek(len(frames))  # 次のフレームに移動
    except EOFError:
        pass

    # 各フレームのサイズを取得
    sprite_width, sprite_height = frames[0].size

    # スプライトシートのサイズを計算
    sheet_width = sprite_width * len(frames)
    sheet_height = sprite_height

    # スプライトシートを作成
    sprite_sheet = Image.new("RGBA", (sheet_width, sheet_height))

    # 各フレームをスプライトシートに貼り付ける
    for i, frame in enumerate(frames):
        sprite_sheet.paste(frame, (i * sprite_width, 0))

    # スプライトシートを保存
    sprite_sheet.save(output_path)

def process_all_gifs(input_dir, output_dir):
    # 入力ディレクトリのすべてのGIFファイルを処理
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.gif'):
            gif_path = os.path.join(input_dir, file_name)
            base_name = os.path.splitext(file_name)[0]
            output_path = os.path.join(output_dir, f"{base_name}_sprite_sheet.png")
            
            # 出力ディレクトリが存在しない場合は作成
            os.makedirs(output_dir, exist_ok=True)
            
            # GIFをスプライトシートに変換
            gif_to_sprite_sheet(gif_path, output_path)
            print(f"Processed {gif_path} -> {output_path}")

# パラメータ設定
input_dir = r"in"  # 入力GIFファイルのディレクトリ
output_dir = r"out"  # 出力スプライトシートのディレクトリ

# 入力ディレクトリのすべてのGIFファイルを処理
process_all_gifs(input_dir, output_dir)
