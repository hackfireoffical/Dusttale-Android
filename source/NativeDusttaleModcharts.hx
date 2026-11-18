package;

import flixel.FlxSprite;
import flixel.group.FlxGroup.FlxTypedGroup;
import flixel.tweens.FlxEase;
import flixel.tweens.FlxTween;

/**
 * Android-native implementation of the non-empty Dusttale song modcharts.
 * The upstream Lua runtime is Windows-only, so these small chart behaviors
 * are reproduced in Haxe for Android instead of attempting to load desktop Lua.
 */
class NativeDusttaleModcharts
{
    private static var defaultY:Float = 0;

    public static function start(song:String, receptors:FlxTypedGroup<FlxSprite>):Void
    {
        if (receptors == null || receptors.members.length < 8) return;

        var normalized = song.toLowerCase().replace(" ", "-");
        defaultY = receptors.members[0].y;

        if (normalized == "last-hope")
        {
            for (i in 0...4)
            {
                var receptor = receptors.members[i];
                FlxTween.tween(receptor, {
                    x: receptor.x - 1000,
                    angle: receptor.angle + 1000
                }, 0.6, {ease: FlxEase.quadOut});
            }

            for (i in 4...8)
            {
                var receptor = receptors.members[i];
                FlxTween.tween(receptor, {
                    x: receptor.x - 275,
                    angle: receptor.angle + 360
                }, 0.6, {ease: FlxEase.quadOut});
            }
        }
    }

    public static function update(song:String, songPosition:Float, bpm:Float, curStep:Int,
        receptors:FlxTypedGroup<FlxSprite>):Void
    {
        if (receptors == null || receptors.members.length < 8) return;

        var normalized = song.toLowerCase().replace(" ", "-");
        var speed:Float = 0;
        var phase:Float = 5.25;
        var amplitude:Float = 10;

        if (normalized == "hallucinations")
        {
            speed = bpm / 200;
            phase = 8.25;
            amplitude = 20;
        }
        else if (normalized == "reality-check")
        {
            if (curStep < 249)
            {
                speed = bpm / 150;
            }
            if (curStep > 238 && curStep < 752)
            {
                speed = bpm / 30;
            }
            if (curStep > 751 && curStep < 1264)
            {
                speed = bpm / 150;
            }
            if (curStep > 1263 && curStep < 1769)
            {
                speed = bpm / 20;
                phase = 20.25;
            }
            if (curStep > 1835)
            {
                speed = bpm / 20;
                phase = 1.25;
                amplitude = 15;
            }
        }

        if (speed == 0) return;

        var currentBeat = (songPosition / 1000) * speed;
        for (i in 0...8)
        {
            receptors.members[i].y = defaultY + amplitude *
                Math.cos((currentBeat + i * phase) * Math.PI);
        }
    }
}
