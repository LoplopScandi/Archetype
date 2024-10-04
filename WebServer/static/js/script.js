// /static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const fileInput = document.querySelector('input[type="file"]');
    
    form.addEventListener('submit', function(event) {
        // ファイルが選択されているかどうかを確認
        if (!fileInput.files.length) {
            alert('ファイルが選択されていません。');
            event.preventDefault();  // フォーム送信を防ぐ
        } else {
            const file = fileInput.files[0];
            // ファイル形式が動画であるかを確認
            if (!file.type.startsWith('video/')) {
                alert('アップロードできるのは動画ファイルのみです。');
                event.preventDefault();  // フォーム送信を防ぐ
            }
        }
    });
});
