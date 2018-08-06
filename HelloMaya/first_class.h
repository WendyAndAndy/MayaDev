//#pragma once

#ifndef __FIRST_CLASS_H__
#define __FIRST_CLASS_H__

#include <maya/MPxCommand.h>
#include <maya/MArgList.h>
#include <maya/MGlobal.h>

namespace WendyAndAndy
{
	class FirstClass : public MPxCommand
	{
	public:
		FirstClass();
		~FirstClass();

		MStatus doIt(const MArgList&);

		static void* creator();
	};
}

#endif // !__FIRST_CLASS_H__

