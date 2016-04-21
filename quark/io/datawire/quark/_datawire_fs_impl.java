package io.datawire.quark.runtime;

import quark.Runtime;
import quark.concurrent.Context;

import java.io.File;
import java.io.FileInputStream;

public class _datawire_fs_impl {
    public static String userHomeDir() {
        return System.getProperty("user.home");
    }

    public static String fileContents(String path) {
        String str = null;
        Runtime runtime = Context.runtime();

        try {
            File file = new File(path);
            FileInputStream fis = new FileInputStream(file);
            byte[] data = new byte[(int) file.length()];

            fis.read(data);
            fis.close();

            str = new String(data, "UTF-8");
        }
        catch (java.io.FileNotFoundException ex) {
            runtime.fail("_datawire_fs.fileContents file not found: " + ex.getMessage());
        }
        catch (java.io.UnsupportedEncodingException ex) {
            runtime.fail("_datawire_fs.fileContents unsupported encoding: " + ex.getMessage());
        }
        catch (java.io.IOException ex) {
            runtime.fail("_datawire_fs.fileContents I/O error: " + ex.getMessage());
        }

        return str;
    }
}
