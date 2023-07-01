function str2code(str){
    if(str === ""){
      return "";
    }
    var arr8 = [];
    var arr16 = [];
    for(var i=0;i<str.length;i++){
      // arr8.push('\\'+str.charCodeAt(i).toString(8)); 
      arr16.push('\\x'+str.charCodeAt(i).toString(16));
    }
    // return arr8.join('');  8进制
    return arr16.join('');
  }

var Unicode = {
	stringify: function (str) {var res = [],
	len = str.length;
	for (var i = 0; i < len; ++i) {res[i] = ("00" + str.charCodeAt(i).toString(16)).slice(-4);
	}

	return str ? "\\u" + res.join("\\u") : "";
	},

	parse: function (str) {str = str.replace(/\\/g, "%");
	return unescape(str);
	}
};

console.log(str2code("<img src=x onerror=alert(1)>123</img>")); //\x61\x61
// console.log(Unicode.stringify("aa")); //\u0061\u0061
