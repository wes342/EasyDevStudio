.class Lcom/android/calculator2/PanelSwitcher;
.super Landroid/widget/FrameLayout;
.source "PanelSwitcher.java"

# interfaces
.implements Landroid/view/animation/Animation$AnimationListener;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/calculator2/PanelSwitcher$Listener;
    }
.end annotation


# static fields
.field private static final ANIM_DURATION:I = 0x190

.field private static final LEFT:I = 0x1

.field private static final MAJOR_MOVE:I = 0x3c

.field private static final RIGHT:I = 0x2


# instance fields
.field private inLeft:Landroid/view/animation/TranslateAnimation;

.field private inRight:Landroid/view/animation/TranslateAnimation;

.field private mChildren:[Landroid/view/View;

.field private mCurrentView:I

.field private mGestureDetector:Landroid/view/GestureDetector;

.field private mListener:Lcom/android/calculator2/PanelSwitcher$Listener;

.field private mPreviousMove:I

.field private mWidth:I

.field private outLeft:Landroid/view/animation/TranslateAnimation;

.field private outRight:Landroid/view/animation/TranslateAnimation;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .locals 2
    .parameter "context"
    .parameter "attrs"

    .prologue
    const/4 v1, 0x0

    .line 56
    invoke-direct {p0, p1, p2}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    .line 36
    new-array v0, v1, [Landroid/view/View;

    iput-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    .line 57
    iput v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    .line 58
    new-instance v0, Landroid/view/GestureDetector;

    new-instance v1, Lcom/android/calculator2/PanelSwitcher$1;

    invoke-direct {v1, p0}, Lcom/android/calculator2/PanelSwitcher$1;-><init>(Lcom/android/calculator2/PanelSwitcher;)V

    invoke-direct {v0, p1, v1}, Landroid/view/GestureDetector;-><init>(Landroid/content/Context;Landroid/view/GestureDetector$OnGestureListener;)V

    iput-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mGestureDetector:Landroid/view/GestureDetector;

    .line 78
    return-void
.end method

.method private updateCurrentView()V
    .locals 3

    .prologue
    .line 94
    iget-object v1, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    array-length v1, v1

    add-int/lit8 v0, v1, -0x1

    .local v0, i:I
    :goto_0
    if-ltz v0, :cond_1

    .line 95
    iget-object v1, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    aget-object v2, v1, v0

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    if-ne v0, v1, :cond_0

    const/4 v1, 0x0

    :goto_1
    invoke-virtual {v2, v1}, Landroid/view/View;->setVisibility(I)V

    .line 94
    add-int/lit8 v0, v0, -0x1

    goto :goto_0

    .line 95
    :cond_0
    const/16 v1, 0x8

    goto :goto_1

    .line 97
    :cond_1
    return-void
.end method


# virtual methods
.method getCurrentIndex()I
    .locals 1

    .prologue
    .line 163
    iget v0, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    return v0
.end method

.method moveLeft()V
    .locals 3

    .prologue
    const/4 v2, 0x1

    .line 138
    iget v0, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    iget-object v1, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    array-length v1, v1

    add-int/lit8 v1, v1, -0x1

    if-ge v0, v1, :cond_0

    iget v0, p0, Lcom/android/calculator2/PanelSwitcher;->mPreviousMove:I

    if-eq v0, v2, :cond_0

    .line 139
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    add-int/lit8 v1, v1, 0x1

    aget-object v0, v0, v1

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/view/View;->setVisibility(I)V

    .line 140
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    add-int/lit8 v1, v1, 0x1

    aget-object v0, v0, v1

    iget-object v1, p0, Lcom/android/calculator2/PanelSwitcher;->inLeft:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v1}, Landroid/view/View;->startAnimation(Landroid/view/animation/Animation;)V

    .line 141
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    aget-object v0, v0, v1

    iget-object v1, p0, Lcom/android/calculator2/PanelSwitcher;->outLeft:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v1}, Landroid/view/View;->startAnimation(Landroid/view/animation/Animation;)V

    .line 142
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    aget-object v0, v0, v1

    const/16 v1, 0x8

    invoke-virtual {v0, v1}, Landroid/view/View;->setVisibility(I)V

    .line 144
    iget v0, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    add-int/lit8 v0, v0, 0x1

    iput v0, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    .line 145
    iput v2, p0, Lcom/android/calculator2/PanelSwitcher;->mPreviousMove:I

    .line 147
    :cond_0
    return-void
.end method

.method moveRight()V
    .locals 3

    .prologue
    const/4 v2, 0x2

    .line 151
    iget v0, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    if-lez v0, :cond_0

    iget v0, p0, Lcom/android/calculator2/PanelSwitcher;->mPreviousMove:I

    if-eq v0, v2, :cond_0

    .line 152
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    add-int/lit8 v1, v1, -0x1

    aget-object v0, v0, v1

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/view/View;->setVisibility(I)V

    .line 153
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    add-int/lit8 v1, v1, -0x1

    aget-object v0, v0, v1

    iget-object v1, p0, Lcom/android/calculator2/PanelSwitcher;->inRight:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v1}, Landroid/view/View;->startAnimation(Landroid/view/animation/Animation;)V

    .line 154
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    aget-object v0, v0, v1

    iget-object v1, p0, Lcom/android/calculator2/PanelSwitcher;->outRight:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v1}, Landroid/view/View;->startAnimation(Landroid/view/animation/Animation;)V

    .line 155
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    aget-object v0, v0, v1

    const/16 v1, 0x8

    invoke-virtual {v0, v1}, Landroid/view/View;->setVisibility(I)V

    .line 157
    iget v0, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    add-int/lit8 v0, v0, -0x1

    iput v0, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    .line 158
    iput v2, p0, Lcom/android/calculator2/PanelSwitcher;->mPreviousMove:I

    .line 160
    :cond_0
    return-void
.end method

.method public onAnimationEnd(Landroid/view/animation/Animation;)V
    .locals 1
    .parameter "animation"

    .prologue
    .line 176
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mListener:Lcom/android/calculator2/PanelSwitcher$Listener;

    if-eqz v0, :cond_0

    .line 177
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mListener:Lcom/android/calculator2/PanelSwitcher$Listener;

    invoke-interface {v0}, Lcom/android/calculator2/PanelSwitcher$Listener;->onChange()V

    .line 179
    :cond_0
    return-void
.end method

.method public onAnimationRepeat(Landroid/view/animation/Animation;)V
    .locals 0
    .parameter "animation"

    .prologue
    .line 168
    return-void
.end method

.method public onAnimationStart(Landroid/view/animation/Animation;)V
    .locals 0
    .parameter "animation"

    .prologue
    .line 172
    return-void
.end method

.method protected onFinishInflate()V
    .locals 4

    .prologue
    .line 117
    invoke-virtual {p0}, Lcom/android/calculator2/PanelSwitcher;->getChildCount()I

    move-result v0

    .line 118
    .local v0, count:I
    new-array v2, v0, [Landroid/view/View;

    iput-object v2, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    .line 119
    const/4 v1, 0x0

    .local v1, i:I
    :goto_0
    if-ge v1, v0, :cond_0

    .line 120
    iget-object v2, p0, Lcom/android/calculator2/PanelSwitcher;->mChildren:[Landroid/view/View;

    invoke-virtual {p0, v1}, Lcom/android/calculator2/PanelSwitcher;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    aput-object v3, v2, v1

    .line 119
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    .line 122
    :cond_0
    invoke-direct {p0}, Lcom/android/calculator2/PanelSwitcher;->updateCurrentView()V

    .line 123
    return-void
.end method

.method public onInterceptTouchEvent(Landroid/view/MotionEvent;)Z
    .locals 1
    .parameter "event"

    .prologue
    .line 133
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mGestureDetector:Landroid/view/GestureDetector;

    invoke-virtual {v0, p1}, Landroid/view/GestureDetector;->onTouchEvent(Landroid/view/MotionEvent;)Z

    move-result v0

    return v0
.end method

.method public onSizeChanged(IIII)V
    .locals 5
    .parameter "w"
    .parameter "h"
    .parameter "oldW"
    .parameter "oldH"

    .prologue
    const-wide/16 v3, 0x190

    const/4 v2, 0x0

    .line 101
    iput p1, p0, Lcom/android/calculator2/PanelSwitcher;->mWidth:I

    .line 102
    new-instance v0, Landroid/view/animation/TranslateAnimation;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mWidth:I

    int-to-float v1, v1

    invoke-direct {v0, v1, v2, v2, v2}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    iput-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->inLeft:Landroid/view/animation/TranslateAnimation;

    .line 103
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->inLeft:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, p0}, Landroid/view/animation/TranslateAnimation;->setAnimationListener(Landroid/view/animation/Animation$AnimationListener;)V

    .line 104
    new-instance v0, Landroid/view/animation/TranslateAnimation;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mWidth:I

    neg-int v1, v1

    int-to-float v1, v1

    invoke-direct {v0, v2, v1, v2, v2}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    iput-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->outLeft:Landroid/view/animation/TranslateAnimation;

    .line 105
    new-instance v0, Landroid/view/animation/TranslateAnimation;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mWidth:I

    neg-int v1, v1

    int-to-float v1, v1

    invoke-direct {v0, v1, v2, v2, v2}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    iput-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->inRight:Landroid/view/animation/TranslateAnimation;

    .line 106
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->inRight:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, p0}, Landroid/view/animation/TranslateAnimation;->setAnimationListener(Landroid/view/animation/Animation$AnimationListener;)V

    .line 107
    new-instance v0, Landroid/view/animation/TranslateAnimation;

    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mWidth:I

    int-to-float v1, v1

    invoke-direct {v0, v2, v1, v2, v2}, Landroid/view/animation/TranslateAnimation;-><init>(FFFF)V

    iput-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->outRight:Landroid/view/animation/TranslateAnimation;

    .line 109
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->inLeft:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v3, v4}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    .line 110
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->outLeft:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v3, v4}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    .line 111
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->inRight:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v3, v4}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    .line 112
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->outRight:Landroid/view/animation/TranslateAnimation;

    invoke-virtual {v0, v3, v4}, Landroid/view/animation/TranslateAnimation;->setDuration(J)V

    .line 113
    return-void
.end method

.method public onTouchEvent(Landroid/view/MotionEvent;)Z
    .locals 1
    .parameter "event"

    .prologue
    .line 127
    iget-object v0, p0, Lcom/android/calculator2/PanelSwitcher;->mGestureDetector:Landroid/view/GestureDetector;

    invoke-virtual {v0, p1}, Landroid/view/GestureDetector;->onTouchEvent(Landroid/view/MotionEvent;)Z

    .line 128
    const/4 v0, 0x1

    return v0
.end method

.method setCurrentIndex(I)V
    .locals 2
    .parameter "current"

    .prologue
    .line 85
    iget v1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    if-eq v1, p1, :cond_1

    const/4 v0, 0x1

    .line 86
    .local v0, changed:Z
    :goto_0
    iput p1, p0, Lcom/android/calculator2/PanelSwitcher;->mCurrentView:I

    .line 87
    invoke-direct {p0}, Lcom/android/calculator2/PanelSwitcher;->updateCurrentView()V

    .line 88
    if-eqz v0, :cond_0

    iget-object v1, p0, Lcom/android/calculator2/PanelSwitcher;->mListener:Lcom/android/calculator2/PanelSwitcher$Listener;

    if-eqz v1, :cond_0

    .line 89
    iget-object v1, p0, Lcom/android/calculator2/PanelSwitcher;->mListener:Lcom/android/calculator2/PanelSwitcher$Listener;

    invoke-interface {v1}, Lcom/android/calculator2/PanelSwitcher$Listener;->onChange()V

    .line 91
    :cond_0
    return-void

    .line 85
    .end local v0           #changed:Z
    :cond_1
    const/4 v0, 0x0

    goto :goto_0
.end method

.method public setListener(Lcom/android/calculator2/PanelSwitcher$Listener;)V
    .locals 0
    .parameter "listener"

    .prologue
    .line 81
    iput-object p1, p0, Lcom/android/calculator2/PanelSwitcher;->mListener:Lcom/android/calculator2/PanelSwitcher$Listener;

    .line 82
    return-void
.end method
