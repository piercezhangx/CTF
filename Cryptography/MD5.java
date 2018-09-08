import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import javax.xml.bind.DatatypeConverter;

public class MD5 {
    public String getSalt() {
        String salt=new String();
        salt = new String()+(1000+(int)(Math.random()*8000-1));
        return salt;
    }

    public String toMD5(String password) {
        String myHash=new String();
        String salt = getSalt();

        password = password+salt;

        System.out.println("Password:"+password);
        System.out.println("Salt:"+salt);
        MessageDigest md;
        try {
            md = MessageDigest.getInstance("MD5");
             md.update(password.getBytes());
                byte[] digest = md.digest();
                myHash = DatatypeConverter
                  .printHexBinary(digest);
        } catch (NoSuchAlgorithmException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
       return myHash;

    }

    public static void main(String[] args) {
        MD5 m = new MD5();
        while (true) {
            String RetHash = m.toMD5("iamnoteasytobreak");
            if (RetHash.equals("AAF8A6D56D4A0AB1E2D1D49329AB6956"))
                break;
        }
        /*
        // TODO Auto-generated method stub
        System.out.println(new MD5().toMD5("iamnoteasytobreak"));
        */
    }
}

/*
 * 该题对密码加了salt, 难度有所提升.
 * 疑惑了一会, 以为是要找到用户密码, 到后来才知道密码已知是让求salt值
 * 这样就简单多了, 用个while 循环匹配HASH 值, 直到匹配上为止.
 * 然后顺利Capture the Flag
 * /

