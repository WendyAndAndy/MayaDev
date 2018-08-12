using Autodesk.Maya.OpenMaya;

[assembly: ExtensionPlugin(typeof(WendyAndAndy.Maya2017CSPlugin))]
[assembly: MPxCommandClass(typeof(WendyAndAndy.HiMayaCmd), "csHi")]

namespace WendyAndAndy
{
    public class Maya2017CSPlugin : IExtensionPlugin
    {
        public string GetMayaDotNetSdkBuildVersion()
        {
            string version = "201780";
            return version;
        }

        public bool InitializePlugin()
        {
            return true;
        }

        public bool UninitializePlugin()
        {
            return true;
        }
    }

    class HiMayaCmd : MPxCommand,IMPxCommand
    {
        public override void doIt(MArgList args)
        {
            MGlobal.displayInfo("你好，Maya2017！The message come from a C# plugin.");
        }
    }
}
