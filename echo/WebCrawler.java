package day_1;


import java.io.*;
import java.net.*;
import java.nio.CharBuffer;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;

public class WebCrawler { 

private static String Text_File_Path = "G:\\data\\htmlsrc.html";

 public static void main(String[] args) throws IOException {
        try { 
        //生成写文件对象 （写文件者需要某个文件对象）
       
        File file = new File(Text_File_Path);
        
        if(!file.exists()) {
        File fileDir = file.getParentFile();
        if(!fileDir.isDirectory()) {
        fileDir.mkdirs();
        }
       
        file.createNewFile();
       
        }
       
FileWriter fpWriter = new FileWriter(file);//需要最后关闭
       
            // 生成下载对象
//连接某台主机的某个端口
            Socket webclient = new Socket("www.bnu.edu.cn", 80); 
            //生成写对象 写到台主机的某个端口
            PrintWriter result = new PrintWriter(webclient.getOutputStream(), true); 
            //生成bufferredreader对象 需要inputstreamreader，需要inputstream
            BufferedReader receiver = new BufferedReader(new InputStreamReader(webclient.getInputStream(),"utf-8"));
            InputStream webInput = webclient.getInputStream();

           //发送HTTP request请求
           result.println("GET / HTTP/1.1"); 
           result.println("Host: bnu.edu.cn"); 
           result.println("Connection: Close"); 
           result.println();
           
           //接收HTTP Response 返回的结果信息        
           boolean bRet = true;
           StringBuilder sBuilder = new StringBuilder(); 
           while (bRet) { 
              if (receiver.ready()) {
            byte[] bytes = new byte[1024];
                int count = 0;
                while (count != -1) {
               
                count = webInput.read(bytes);
           
                String tempStr = new String(bytes,"utf-8");
                System.out.println(tempStr);
                sBuilder.append(tempStr);
                }
                bRet = false; 
            } 
          }
           
          // 显示获得的网页正文，打印到控制台  
          //System.out.println(new String(sBuffer.toString().getBytes("gbk"),"utf-8"));
          //System.out.println(sBuilder.toString());
          fpWriter.write(sBuilder.toString());
          webclient.close();
          fpWriter.close();
       } catch (UnknownHostException e) {
            System.err.println("无法访问指定主机."); 
            System.exit(1);
       } catch (IOException e) { 
           System.err.println("下载失败，请检查输入地址是否正确。");  
           System.exit(1);
       } 
        
  }
        
 
}