var initFromBaseModules = function(baseModules){
    return $.extend.apply({}, [true].concat(baseModules || []))
};


var config = {
        title: '确定继续吗',
        type: 'warning',
        showCancelButton: true,
        cancelButtonText: '取消',
        confirmButtonColor: '#DD6B55',
        confirmButtonText: '确定',
        closeOnConfirm: false
    };


var form = (function(baseModules) {
    var mod = initFromBaseModules(baseModules);
    mod.getFormDataMapping = function($form){
        var dataArray = $form.formToArray();//jquery.form.js
        var dataDic = {};
        $.each(dataArray, function(index, data){
            if(!!dataDic[data.name]){
                dataDic[data.name].push(data.value);
            }
            else
                dataDic[data.name] = [data.value];
        });

        // var dataMapping = {};
        // $.each(dataDic, function(name, value){
        //     dataMapping[name] = $.md5(value.sort().join(''));//jquery.md5.js
        // });
        return dataDic
    };

    mod.getSameFields = function(data1, data2){
        var fields = [];
		$.each(data1, function(name1, value1){
			var value2 = data2[name1];
			if (!!value2 && value2 == value1) {
				fields.push(name1);
			}
		});
		return fields;
	};

    // mod.request = function ($form, method, callback, errorCallback, customOptions) {
	// 	var options = initOptions(method, callback, errorCallback, customOptions);
	// 	$form.ajaxSubmit(options);
	// };

    return mod;
}());

(function(){
    $.fn.ajaxFormDialog = function (callback, errorCallback, customCallback) {
        var $form = $(this);
        var initFormDataMapping = form.getFormDataMapping($form);
        $form.find('[type=submit]').click(function () {
            var ele = $('#textarea-content');
            if (ele.length) {
                var htmlStr = KindEditor.instances[0].html().trim();
                $('#textarea-content').val(htmlStr);
            }
            if (!$form.valid()) {
                return false;
            }
            submitHandler(callback, errorCallback, customCallback);
            return false;
        });

        var submitHandler = function(callback, errorCallback, customCallback){
            var currentDataMapping = form.getFormDataMapping($form);
            var sameFields = form.getSameFields(initFormDataMapping, currentDataMapping);
            $.each(sameFields, function(index, value){
                delete currentDataMapping[value];
            });

            swal(config, function () {
            var options = {
                success: function () {
                    callback();
                },
                data: currentDataMapping,
                type: $form.attr('method')
            };
            $form.ajaxSubmit(options);
        })};
        };
}());