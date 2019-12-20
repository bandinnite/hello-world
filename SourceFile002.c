#pragma config(Motor,  port1,           RD,            tmotorVex393_HBridge, openLoop, encoderPort, None)
#pragma config(Motor,  port2,           LD,            tmotorVex393_HBridge, openLoop, encoderPort, None)
#pragma config(Motor,  port3,           Shoot,         tmotorVex393_HBridge, openLoop, encoderPort, None)
#pragma config(Motor,  port4,           Intake,        tmotorVex393_HBridge, openLoop, encoderPort, None)
#pragma config(Motor,  port5,           gate,          tmotorServoStandard, openLoop)

task main()
{
	int intt;
	intt = 0;
	while(true)
	{
		motor(LD)=(vexRT[Ch3]);
		motor(RD)=(vexRT[Ch2]);
		if (vexRT[Btn8U] == true)
		{
			if (intt == 1)
			{
				intt = 0;
				motor(Intake)=0;
			}
			if (intt == 0)
			{
				intt = 1;
				motor(Intake)=127;
			}
		}
	}
}
