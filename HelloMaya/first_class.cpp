#include "first_class.h"

namespace WendyAndAndy
{
	FirstClass::FirstClass()
	{
		MGlobal::displayInfo("FirstClass constructor");
	}

	FirstClass::~FirstClass()
	{
		MGlobal::displayInfo("FirstClass deConstructor");
	}

	MStatus FirstClass::doIt(const MArgList &args)
	{
		MGlobal::displayInfo("Hello, Maya (from FirstClass)");

		return MS::kSuccess;
	}

	void *FirstClass::creator()
	{
		return new FirstClass;
	}
}