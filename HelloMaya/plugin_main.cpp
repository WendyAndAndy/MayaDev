#include "first_class.h"
#include <maya/MGlobal.h>
#include <maya/MPxCommand.h>
#include <maya/MFnPlugin.h>
#include <maya/MString.h>
#include <maya/MArgList.h>
#include <maya/MObject.h>

#define __VENDOR "kingmax_res@163.com | 184327932@qq.com | iJasonLee@WeChat"
#define __VERSION "2018.08.06.01"

namespace WendyAndAndy
{
	class SecondClass : public MPxCommand
	{
	public:
		SecondClass() = default;
		~SecondClass() = default;

		MStatus doIt(const MArgList &args)
		{
			MGlobal::displayInfo("SecondClass say hello");
			return MS::kSuccess;
		}

		static void* creator()
		{
			return new SecondClass();
		}
	};
}

//加载插件时注册命令、节点等
MStatus initializePlugin(MObject obj)
{
	MFnPlugin plugin(obj, __VENDOR, __VERSION);
	MStatus status;
	status = plugin.registerCommand("myCmd1", WendyAndAndy::FirstClass::creator); //命令的名字可以随便定义
	if (!status)
		status.perror("register command myCmd1 failed");

	//注册第二条命令
	status = plugin.registerCommand("hello", WendyAndAndy::SecondClass::creator); //命令的名字可以随便定义
	if (!status)
		status.perror("register command hello failed");

	return MS::kSuccess;
}

//卸载插件时取消注册
MStatus uninitializePlugin(MObject obj)
{
	MFnPlugin plugin(obj, __VENDOR, __VERSION);
	MStatus status;
	//取消注册
	status = plugin.deregisterCommand("myCmd1"); //命令的名字与前面定义的一致
	if (!status)
		status.perror("deregister command myCmd1 failed");

	//注册第二条命令
	status = plugin.deregisterCommand("hello"); //命令的名字与前面定义的一致
	if (!status)
		status.perror("deregister command hello failed");

	return MS::kSuccess;
}