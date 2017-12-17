KindEditor.ready(function (k) {
    k.create('#textarea-content', {
        width: '500',
        height: '500',
        uploadJson: '/admin/upload/kindeditor'
    })
});