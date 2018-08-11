using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Autodesk.Maya.Runtime; //Maya2014
using Autodesk.Maya.OpenMaya;

/***
 * In the .NET SDK of Maya, .NET assembly attributes are used to auto-register plug-ins, commands, nodes and so forth. 
 * This is different from the C++ SDK of Maya, 
 * where the MFnPlugin class provides registration methods for all MPx-prefixed classes of Maya (MPxCommand, MPxNode, and so forth).
***/

[assembly: ExtensionPlugin(typeof(WendyAndAndy.MayaCSPlugin), "184327932@qq.com", "2018.08.11.01", "any")] //Maya2014
//[assembly: ExtensionPlugin(typeof(WendyAndAndy.MayaCSPlugin))]
[assembly: MPxCommandClass(typeof(WendyAndAndy.CSHelloMaya), "csHiMaya")]

namespace WendyAndAndy
{
    public class MayaCSPlugin : IExtensionPlugin
    {
        public string GetMayaDotNetSdkBuildVersion()
        {
            return "201414";
        }

        public bool InitializePlugin()
        {
            MGlobal.displayInfo("MayaCSPlugin initialize");
            return true;
        }

        public bool UninitializePlugin()
        {
            MGlobal.displayInfo("MayaCSPlugin uninitialize");
            return true;
        }
    }

    public class CSHelloMaya: MPxCommand, IMPxCommand
    {
        public override void doIt(MArgList args)
        {
            MGlobal.displayInfo("Hello, Maya. This is a C# Maya Plugin. 中文测试：你好，妈呀！");
        }
    }
}
