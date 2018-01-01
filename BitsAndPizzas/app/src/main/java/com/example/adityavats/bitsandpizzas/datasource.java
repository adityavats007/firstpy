package com.example.adityavats.bitsandpizzas;

/**
 * Created by Adityavats on 3/14/2017.
 */


public class datasource {
    private String name;
    private String description;
    public static final datasource[] data= {
            new datasource("INTRODUCTION","Android provides a rich application framework that allows you to build innovative apps and games for mobile devices in a Java language environment. The documents listed in the left navigation provide details about how to build apps using Android's various APIs.\n" +
                    "\n" +
                    "If you're new to Android development, it's important that you understand the following fundamental concepts about the Android app framework:\n" +
                    "\n" +
                    "Apps provide multiple entry points\n" +
                    "Android apps are built as a combination of distinct components that can be invoked individually. For instance, an individual activity provides a single screen for a user interface, and a service independently performs work in the background.\n" +
                    "\n" +
                    "From one component you can start another component using an intent. You can even start a component in a different app, such as an activity in a maps app to show an address. This model provides multiple entry points for a single app and allows any app to behave as a user's \"default\" for an action that other apps may invoke.\n" +
                    "\n" +
                    "Learn more:\n" +
                    "\n" +
                    "App Fundamentals\n" +
                    "Intents and Intent Filters\n" +
                    "Activities\n" +
                    "Apps adapt to different devices\n" +
                    "Android provides an adaptive app framework that allows you to provide unique resources for different device configurations. For example, you can create different XML layout files for different screen sizes and the system determines which layout to apply based on the current device's screen size.\n" +
                    "\n" +
                    "You can query the availability of device features at runtime if any app features require specific hardware such as a camera. If necessary, you can also declare features your app requires so app markets such as Google Play Store do not allow installation on devices that do not support that feature."),
            new datasource("PLATFORM ARCHITECTURE","zesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzgezesgdvzge"),
            new datasource("APP COMPONENTS",""),
            new datasource("APP RESOURCES",""),
            new datasource("APP MANIFESTS",""),
            new datasource("APP MANIFESTS",""),
            new datasource("USER INTERFACE",""),
            new datasource("ANIMATION AND GRAPHICS",""),
            new datasource("COMPUTATION",""),
            new datasource("MEDIA APPS",""),
            new datasource("MEDIA APPS",""),
            new datasource("MEDIA APPS",""),
            new datasource("MEDIA APPS",""),
            new datasource("MEDIA APPS",""),new datasource("MEDIA APPS",""),

            new datasource("MEDIA APPS","")

    };
    private datasource(String name,String description){
        this.name=name;
        this.description=description;
    }
    public String getDescription(){
        return description;
    }
    public String getName(){
        return name;
    };
    public String toString(){
        return this.name;
    }
}
